from setuptools import setup, find_packages

setup(name='isotoma.zope.aqheaders',
      version="0.0.2",
      url="http://www.isotoma.com/",
      author="Richard Mitchell",
      author_email="richard.mitchell@isotoma.com",
      description="Adds HTTP headers about Acquisition to responses from Zope.",
      long_description="\n".join([open(f).read() for f in 
          (
          'README.rst',
          'HISTORY.rst',
          'LICENSE.rst'
          )]),
      license='Apache License, Version 2.0',
      packages=find_packages(),
      install_requires=[
          'Acquisition',
          'z3c.autoinclude',
          'zope.app.publisher'
          ],
      zip_safe=False,
      include_package_data=True,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Zope2',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Debuggers',
          'Topic :: Software Development :: Testing',
          ]
)
