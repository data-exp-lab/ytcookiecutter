===============
dxlcookiecutter
===============

This is an experimental Cookiecutter_ template for yt-related development, including rapid prototyping of new frontends.

* GitHub repo: https://github.com/chrishavlin/dxlcookiecutter/
* Documentation: https://dxlcookiecutter.readthedocs.io/
* Free software: BSD license

Features
--------

In addition to the `standard cookiecutter template <https://github.com/audreyfeldroy/cookiecutter-pypackage/>`_ features, this template includes:

* frontend scaffolding
* github actions for build tests
* pre-commit configuration
* auto-generation of requirements files with yt-related dependencies

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Build Status
-------------

Quickstart
----------

To use, first install cookiecutter and some extra dependencies needed for template generation:

    pip install cookiecutter pyyaml PyGithub

and then to use this template:

    cookiecutter https://github.com/chrishavlin/dxlcookiecuttertest.git

this will generate a new package directory. TO DO: write more.

Maintainer Notes
----------------

This repository is itself a package, `dxlcookiecutter`, that includes some tools for auto-generation of cookiecutter templates. It can be installed with

    $ pip install -e .

after which you can (re)-generate templates using the command line. To view the options:

    $ dxlcookiecutter -h

and running

    $ dxlcookiecutter stream-template

will build the template for the stream frontend data loaders.
