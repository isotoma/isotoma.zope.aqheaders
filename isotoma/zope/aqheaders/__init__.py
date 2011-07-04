""" See README.rst and LICENSE.rst in the root of this package for more
    information.
"""

from copy import copy

from Acquisition import aq_base, aq_chain, aq_inner, aq_parent
from OFS.interfaces import ITraversable


def add_acquisition_headers(ob, event):
    """ Added as an event handler for the IBeforeTraversal event by
        configure.zcml.

        If the result of the current URI has been a result of
        acquisition, adds a HTTP header to the response, X-Acquired-Path
        with the actual, physical path to the resource.

        If any acquisition used has been redundant (i.e. some object has
        been acquired via itself), an extra header,
        X-Acquired-Redundantly is added to the response with a value of
        'True'.
    """

    request = event.request
    stack = copy(request.get('TraversalRequestNameStack', []))
    if not stack:
        return

    stack.reverse()
    marker = object()
    result = ob.unrestrictedTraverse(stack, marker)
    __traceback_info__ = stack, result
    
    ctx = result
    if not ITraversable.providedBy(ctx):
        ctx = getattr(ctx, 'im_self', 
                      getattr(ctx, 'context', ctx)
                      )

    acquired = False
    chain = aq_chain(ctx)
    if len(chain) > len(set(chain)):
        acquired = True
        request.response.addHeader('X-Acquired-Redundantly', 'True')

    if ctx is not marker and \
       ITraversable.providedBy(ctx):

        if not acquired:
            for i in chain:
                context = aq_parent(i)
                container = aq_parent(aq_inner(i))
                if aq_base(context) is not aq_base(container):
                    acquired = True
                    break

        acquired_path = ctx.absolute_url_path()
        if ctx != result and hasattr(result, '__name__'):
            acquired_path = '%s/%s' % (acquired_path, result.__name__)

        if acquired:
            request.response.addHeader('X-Acquired-Path', acquired_path)