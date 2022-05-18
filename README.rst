###################
pyproject-examples
###################

.. start short_desc

**Example pyproject.toml configs for testing.**

.. end short_desc

These are designed to be used in the testsuite for
`pyproject-parser <https://github.com/repo-helper/pyproject-parser>`_
and `whey <https://github.com/repo-helper/whey>`_,
but may be useful for other tools based on those.

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |actions_linux| image:: https://github.com/repo-helper/pyproject-examples/workflows/Linux/badge.svg
	:target: https://github.com/repo-helper/pyproject-examples/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/repo-helper/pyproject-examples/workflows/Windows/badge.svg
	:target: https://github.com/repo-helper/pyproject-examples/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/repo-helper/pyproject-examples/workflows/macOS/badge.svg
	:target: https://github.com/repo-helper/pyproject-examples/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/repo-helper/pyproject-examples/workflows/Flake8/badge.svg
	:target: https://github.com/repo-helper/pyproject-examples/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/repo-helper/pyproject-examples/workflows/mypy/badge.svg
	:target: https://github.com/repo-helper/pyproject-examples/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.herokuapp.com/github/repo-helper/pyproject-examples/badge.svg
	:target: https://dependency-dash.herokuapp.com/github/repo-helper/pyproject-examples/
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/repo-helper/pyproject-examples?logo=codefactor
	:target: https://www.codefactor.io/repository/github/repo-helper/pyproject-examples
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/pyproject-examples
	:target: https://pypi.org/project/pyproject-examples/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyproject-examples?logo=python&logoColor=white
	:target: https://pypi.org/project/pyproject-examples/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyproject-examples
	:target: https://pypi.org/project/pyproject-examples/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/pyproject-examples
	:target: https://pypi.org/project/pyproject-examples/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/repo-helper/pyproject-examples
	:target: https://github.com/repo-helper/pyproject-examples/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/repo-helper/pyproject-examples
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/repo-helper/pyproject-examples/v2022.5.18
	:target: https://github.com/repo-helper/pyproject-examples/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/repo-helper/pyproject-examples
	:target: https://github.com/repo-helper/pyproject-examples/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2022
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/pyproject-examples
	:target: https://pypi.org/project/pyproject-examples/
	:alt: PyPI - Downloads

.. end shields

Installation
--------------

.. start installation

``pyproject-examples`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install pyproject-examples

.. end installation


Usage
--------

``pyproject-examples`` provides the following API:


``pyproject_examples`` module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``valid_pep621_config``
*************************

A list of `pytest params`_ for valid ``pyproject.toml`` files per `PEP 621`_.
The params contain the ``pyproject.toml`` content as a string.
Each param has its own unique ID, which can be seen in the source
`here <https://github.com/repo-helper/pyproject-examples/blob/master/pyproject_examples/__init__.py#L68>`__.

.. _pytest params: https://docs.pytest.org/en/6.2.x/reference.html#pytest-param:
.. _PEP 621: https://peps.python.org/pep-0621/


``bad_pep621_config``
*************************

A list of `pytest params`_ for invalid ``pyproject.toml`` files per `PEP 621`_.
Each param contains the ``pyproject.toml`` content (as a string),
the expected Python exception (for catching with `pytest.raises`_), and the expected exception text (for passing as the ``match`` argument to ``pytest.raises``.
Each param also has its own unique ID, which can be seen in the source `here <https://github.com/repo-helper/pyproject-examples/blob/master/pyproject_examples/__init__.py#L88>`__.

.. _pytest.raises: https://docs.pytest.org/en/6.2.x/reference.html#pytest.raises


``valid_buildsystem_config``
*******************************

A list of `pytest params`_ for valid ``[build-system]`` tables from ``pyproject.toml`` files per `PEP 517`_ and `PEP 517`_.
The params contain the ``pyproject.toml`` content as a string.
Each param has its own unique ID, which can be seen in the source
`here <https://github.com/repo-helper/pyproject-examples/blob/master/pyproject_examples/__init__.py#L191>`__.

.. _PEP 517: https://peps.python.org/pep-0517/
.. _PEP 518: https://peps.python.org/pep-0518/


``bad_buildsystem_config``
****************************

A list of `pytest params`_ for invalid ``[build-system]`` tables from ``pyproject.toml`` files per `PEP 517`_ and `PEP 517`_.
Each param contains the ``pyproject.toml`` content (as a string),
the expected Python exception (for catching with `pytest.raises`_), and the expected exception text (for passing as the ``match`` argument to ``pytest.raises``.
Each param also has its own unique ID, which can be seen in the source `here <https://github.com/repo-helper/pyproject-examples/blob/master/pyproject_examples/__init__.py#206>`__.


``pyproject_examples.example_configs`` submodule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the example configuration files themselves.
Each file is stored as a string.

The configuration files are:

* ``MINIMAL_CONFIG``
* ``KEYWORDS``
* ``AUTHORS``
* ``UNICODE``
* ``MAINTAINERS``
* ``CLASSIFIERS``
* ``DEPENDENCIES``
* ``OPTIONAL_DEPENDENCIES``
* ``OPTIONAL_DEPENDENCIES_EMPTY_GROUP``
* ``URLS``
* ``ENTRY_POINTS``
* ``COMPLETE_PROJECT_A``
* ``COMPLETE_A``
* ``COMPLETE_B``
* ``COMPLETE_A_WITH_FILES``
* ``DYNAMIC_REQUIREMENTS``
* ``LONG_REQUIREMENTS``


``pyproject_examples.utils`` submodule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains utility functions.

``file_not_found_regex(filename: str) -> str``
************************************************

This function create a regular expression for testing ``FileNotFoundError``\s.

This is useful for testing error messages between Windows and POSIX, as well as between CPython and PyPy.

**filename** The filename which can't be found.
