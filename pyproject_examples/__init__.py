#!/usr/bin/env python3
#
#  __init__.py
"""
Example pyproject.toml configs for testing.
"""
# stdlib
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#
import re

# 3rd party
import pytest as pytest
from coincidence.selectors import not_windows, only_windows
from dom_toml.parser import BadConfigError

# this package
from pyproject_examples.example_configs import (
		AUTHORS,
		CLASSIFIERS,
		COMPLETE_A,
		COMPLETE_B,
		COMPLETE_PROJECT_A,
		DEPENDENCIES,
		ENTRY_POINTS,
		KEYWORDS,
		MAINTAINERS,
		MINIMAL_CONFIG,
		OPTIONAL_DEPENDENCIES,
		OPTIONAL_DEPENDENCIES_EMPTY_GROUP,
		UNICODE,
		URLS
		)
from pyproject_examples.utils import file_not_found_regex

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2021 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "2022.5.3"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = [
		"valid_pep621_config",
		"bad_pep621_config",
		"valid_buildsystem_config",
		"bad_buildsystem_config",
		]

valid_pep621_config = [
		pytest.param(MINIMAL_CONFIG, id="minimal"),
		pytest.param(f'{MINIMAL_CONFIG}\ndescription = "Lovely Spam! Wonderful Spam!"', id="description"),
		pytest.param(f'{MINIMAL_CONFIG}\nrequires-python = ">=3.8"', id="requires-python"),
		pytest.param(f'{MINIMAL_CONFIG}\nrequires-python = ">=2.7,!=3.0.*,!=3.2.*"', id="requires-python_complex"),
		pytest.param(KEYWORDS, id="keywords"),
		pytest.param(AUTHORS, id="authors"),
		pytest.param(MAINTAINERS, id="maintainers"),
		pytest.param(CLASSIFIERS, id="classifiers"),
		pytest.param(DEPENDENCIES, id="dependencies"),
		pytest.param(OPTIONAL_DEPENDENCIES, id="optional-dependencies"),
		pytest.param(OPTIONAL_DEPENDENCIES_EMPTY_GROUP, id="optional-dependencies-empty-group"),
		pytest.param(URLS, id="urls"),
		pytest.param(ENTRY_POINTS, id="entry_points"),
		pytest.param(UNICODE, id="unicode"),
		pytest.param(COMPLETE_PROJECT_A, id="COMPLETE_PROJECT_A"),
		pytest.param(COMPLETE_A, id="COMPLETE_A"),
		pytest.param(COMPLETE_B, id="COMPLETE_B"),
		]

bad_pep621_config = [
		# pytest.param(
		# 		'[project]\nname = "spam"',
		# 		BadConfigError,
		# 		"The 'project.version' field must be provided.",
		# 		id="no_version"
		# 		),
		pytest.param(
				'[project]\n\nversion = "2020.0.0"',
				BadConfigError,
				"The 'project.name' field must be provided.",
				id="no_name"
				),
		pytest.param(
				'[project]\ndynamic = ["name"]',
				BadConfigError,
				"The 'project.name' field may not be dynamic.",
				id="dynamic_name"
				),
		pytest.param(
				'[project]\nname = "???????12345=============☃"\nversion = "2020.0.0"',
				BadConfigError,
				"The value for 'project.name' is invalid.",
				id="bad_name"
				),
		pytest.param(
				'[project]\nname = "spam"\nversion = "???????12345=============☃"',
				BadConfigError,
				re.escape("Invalid version: '???????12345=============☃'"),
				id="bad_version"
				),
		pytest.param(
				f'{MINIMAL_CONFIG}\nrequires-python = "???????12345=============☃"',
				BadConfigError,
				re.escape("Invalid specifier: '???????12345=============☃'"),
				id="bad_requires_python"
				),
		pytest.param(
				f'{MINIMAL_CONFIG}\nauthors = [{{name = "Bob, Alice"}}]',
				BadConfigError,
				r"The 'project.authors\[0\].name' key cannot contain commas.",
				id="author_comma"
				),
		pytest.param(
				f'{MINIMAL_CONFIG}\nmaintainers = [{{name = "Bob, Alice"}}]',
				BadConfigError,
				r"The 'project.maintainers\[0\].name' key cannot contain commas.",
				id="maintainer_comma"
				),
		pytest.param(
				f'{MINIMAL_CONFIG}\nkeywords = [1, 2, 3, 4, 5]',
				TypeError,
				r"Invalid type for 'project.keywords\[0\]': expected <class 'str'>, got <class 'int'>",
				id="keywords_wrong_type"
				),
		pytest.param(
				f'{MINIMAL_CONFIG}\nclassifiers = [1, 2, 3, 4, 5]',
				TypeError,
				r"Invalid type for 'project.classifiers\[0\]': expected <class 'str'>, got <class 'int'>",
				id="classifiers_wrong_type"
				),
		pytest.param(
				f'{MINIMAL_CONFIG}\ndependencies = [1, 2, 3, 4, 5]',
				TypeError,
				r"Invalid type for 'project.dependencies\[0\]': expected <class 'str'>, got <class 'int'>",
				id="dependencies_wrong_type"
				),
		pytest.param(
				f'{MINIMAL_CONFIG}\nreadme = "README.rst"',
				FileNotFoundError,
				r"No such file or directory: ((Windows|Posix)Path(Plus)?\('README.rst'\)|'README.rst')",
				id="missing_readme_file",
				marks=not_windows("Message differs on Windows.")
				),
		pytest.param(
				f'{MINIMAL_CONFIG}\nlicense = {{file = "LICENSE.txt"}}',
				FileNotFoundError,
				r"No such file or directory: ((Windows|Posix)Path(Plus)?\('LICENSE.txt'\)|'LICENSE.txt')",
				id="missing_license_file",
				marks=not_windows("Message differs on Windows.")
				),
		pytest.param(
				f'{MINIMAL_CONFIG}\nreadme = "README.rst"',
				FileNotFoundError,
				file_not_found_regex("README.rst"),
				id="missing_readme_file_win32",
				marks=only_windows("Message differs on Windows.")
				),
		pytest.param(
				f'{MINIMAL_CONFIG}\nlicense = {{file = "LICENSE.txt"}}',
				FileNotFoundError,
				file_not_found_regex("LICENSE.txt"),
				id="missing_license_file_win32",
				marks=only_windows("Message differs on Windows.")
				),
		pytest.param(
				f"{MINIMAL_CONFIG}\n[project.urls]\na_really_long_label_which_exceeds_32_characters = 'example.com'",
				ValueError,
				r"'project.urls.a_really_long_label_which_exceeds_32_characters': label too long \(max 32 characters\)",
				id="label_too_long",
				),
		]

valid_buildsystem_config = [
		pytest.param('[build-system]\nrequires = []', id="requires_nothing"),
		pytest.param('[build-system]\nrequires = ["whey"]', id="requires_whey"),
		pytest.param('[build-system]\nrequires = ["setuptools", "wheel"]', id="requires_setuptools"),
		pytest.param('[build-system]\nrequires = ["whey"]\nbuild-backend = "whey"', id="complete"),
		pytest.param(
				'[build-system]\nrequires = ["whey"]\nbuild-backend = "whey"\nbackend-path = ["../foo"]',
				id="backend_path"
				),
		pytest.param(
				'[build-system]\nrequires = ["whey"]\nbuild-backend = "whey"\nbackend-path = ["../foo", "./bar"]',
				id="backend_paths"
				),
		]

bad_buildsystem_config = [
		pytest.param(
				'[build-system]\nbackend-path = ["./foo"]',
				BadConfigError,
				"The 'build-system.requires' field must be provided.",
				id="no_requires"
				),
		pytest.param(
				'[build-system]\nrequires = [1234]',
				TypeError,
				r"Invalid type for 'build-system.requires\[0\]': expected <class 'str'>, got <class 'int'>",
				id="requires_list_int"
				),
		pytest.param(
				'[build-system]\nrequires = "whey"',
				TypeError,
				"Invalid type for 'build-system.requires': expected <class 'collections.abc.Sequence'>, got <class 'str'>",
				id="requires_str"
				),
		pytest.param(
				'[build-system]\nrequires = ["whey"]\nbackend-path = [1234]',
				TypeError,
				r"Invalid type for 'build-system.backend-path\[0\]': expected <class 'str'>, got <class 'int'>",
				id="backend_path_list_int"
				),
		pytest.param(
				'[build-system]\nrequires = ["whey"]\nbackend-path = "whey"',
				TypeError,
				"Invalid type for 'build-system.backend-path': expected <class 'collections.abc.Sequence'>, got <class 'str'>",
				id="backend_path_str"
				),
		pytest.param(
				'[build-system]\nrequires = ["whey"]\nbackend-path = ["whey"]',
				BadConfigError,
				"'build-system.backend-path' cannot be specified without also specifying 'build-system.build-backend'",
				id="backend_path_without_backend"
				),
		]
