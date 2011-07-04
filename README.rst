======================
isotoma.zope.aqheaders
======================

Adds HTTP headers about Acquisition to responses from Zope.

If the response to the request results from Acquisition in any way, the
``X-Acquired-Path`` header is added with the physical path to the
content served as its value.

If the Acquisition chain used to determine the request response
contains some redundant part (see examples below), then the
``X-Acquired-Redundantly``` header is added to the response with the
string value of ``True``.

Purpose
=======

This product was originally devised to aid debugging and to be used to
prevent spiders or link-checkers processing an endless series of
URIs which are only made possible by Acquisition.

Examples
========

Consider the tree:
 * ``App``
  - ``Plone``
    + ``foo``
    + ``bar``
    + ``baz``
      * ``qux``
      * ``quux``

Example 1
---------
:Request URI:      /Plone/foo
:Response headers: -

Example 2
---------
:Request URI:      /Plone/foo/bar
:Response headers:
                   ``X-Acquired-Path``: ``/Plone/bar``

The Acquired path header is provided because ``bar`` is acquired via ``foo``.

Example 3
---------
:Request URI:      /Plone/foo/foo/bar
:Response headers:
                   ``X-Acquired-Path``:        ``/Plone/bar``
                   ``X-Acquired-Redundantly``: ``True``

The Acquired redundantly header is provided because ``foo`` is acquired via itself.
The Acquired path header is provided because ``bar`` is acquired via ``foo``.

Example 4
---------
:Request URI:      /Plone/baz/qux/quux/baz/foo
:Response headers:
                   ``X-Acquired-Path``: ``/Plone/foo``
                   ``X-Acquired-Redundantly``: ``True``

The Acquired redundantly header is provided because ``baz`` is acquired via itself.
The Acquired path header is provided because ``foo`` is acquired via ``baz``.

Example 5
---------
:Request URI:      /Plone/foo/baz/getId
:Response headers:
                   ``X-Acquired-Path``: ``/Plone/baz/getId``

The Acquired path header is provided because ``baz/getId`` is acquired via ``foo``.
