.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://github.com/collective/collective.cleanuprevisions/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/collective.cleanuprevisions/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/collective.cleanuprevisions/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/collective.cleanuprevisions?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/collective.cleanuprevisions/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/collective.cleanuprevisions

.. image:: https://img.shields.io/pypi/v/collective.cleanuprevisions.svg
    :target: https://pypi.python.org/pypi/collective.cleanuprevisions/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.cleanuprevisions.svg
    :target: https://pypi.python.org/pypi/collective.cleanuprevisions
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.cleanuprevisions.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.cleanuprevisions.svg
    :target: https://pypi.python.org/pypi/collective.cleanuprevisions/
    :alt: License


===========================
collective.cleanuprevisions
===========================

Delete content revisions (versions)

Features
--------

- provides a view @@clean-revisions


Installation
------------

Install collective.cleanuprevisions by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.cleanuprevisions


and then running ``bin/buildout``

Usage
-----

- first set the desired value in /portal_purgepolicy
- call the view `@@clean-revisions`


Authors
-------

- MrTango - Maik Derstappen - md@derico.de


Contributors
------------

Put your name here, you deserve it!

- ?


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.cleanuprevisions/issues
- Source Code: https://github.com/collective/collective.cleanuprevisions


Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under the GPLv2.
