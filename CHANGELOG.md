# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [v0.1.10] - 2025-08-12
### Changed
- `README.ja.md`: 
  - Corrected the typo in the file name "README.md". README.ja.md->README.md

## [v0.1.9] - 2025-08-12
### Changed
- `README.md`: 
  - Corrected the link destination.
- `README.ja.md`: 
  - Corrected the link destination.

## [v0.1.8] - 2025-08-11
### Changed
- `examples/sample_ini_parser.py`: 
  - Fixed pip install command for ini_cfg_parser.
  - Removed unused configparser.
- `README.md`: 
  - Fixed to be able to switch between Japanese and English.
  - Added Tested Environments.
### Added
- `README.ja.md`: 
- `tests/requirements.txt`: 

## [v0.1.7] - 2025-07-01
### Fixed
- `ini_cfg_parser/ini_cfg_parser.py`: 
  - Fixed a bug where unnecessary half-width characters were included when there were half-width spaces before and after the comma (,) when type was List[str].
### Changed
- `ini_cfg_parser/ini_cfg_parser.py`: 
  - Supports "csv format" when the type is List[int], List[float], or List[bool].
- `tests/test_ini_parser.py`: 
  - def test_ini_setting_csvfmt(): Added a test for list type.

## [v0.1.6] - 2025-06-30
### Changed
- `ini_cfg_parser/ini_cfg_parser.py`: 
  - When type is List[str], it is now compatible with "csv format".  It is now compatible with strings containing "," enclosed in double quotation marks.
  - Create a self.parsed_val variable to store the information.
- `tests/test_ini_parser.py`: 
  - def test_ini_setting_csvfmt(): Added
  - def test_parsed_val(): Added
- `examples/sample_ini_parser.py`: 
  - Corrected the example to use the variable parsed_val.
  - Removed the version check process.

## [v0.1.5] - 2025-06-26
### Changed
- `ini_cfg_parser/ini_cfg_parser.py`: 
  - Removed unused import process for libirar packaging.
- `tests/test_ini_parser.py`: 
  - def test_is_valid_ini_dict(): Added
  - def test_is_valid_ini_value(): Added
  - def test_set_use_def_val(): Added
  - def test_set_fallback_def_val(): Added
  - def test_die_print(capsys): Added
- `setup.cfg`:
  - Removed 'packaging' from install_requires.

## [v0.1.4] - 2025-06-25
### Changed
- `setup.cfg`: 
  - Changed python_requires from 3.10 to 3.8.
- `ini_cfg_parser/ini_cfg_parser.py`: 
  - `match` statements have been changed to `if` statements. Reason=To accommodate a wider range of Python environments.

## [v0.1.3] - 2025-06-25
###Fixed
- `ini_cfg_parser/ini_cfg_parser.py`: 
  - def write_inifile(): Modified to prevent the information in the DEFAULT section from being copied to other sections.
### Changed
- `README.md`: Added explanation.
- `ini_cfg_parser/ini_cfg_parser.py`: 
  - def _get_value(): Modified to allow information from the ini file to be obtained even if there is no information in ini_dict.
  - def add_section(): Added
  - def add_ini_dict_keys(): Added
- `tests/test_ini_parser.py`: 
  - def test_nosection_set(): Added
  - def test_no_inidict(): Added

## [v0.1.2] - 2025-06-21
### Changed
- `ini_cfg_parser/ini_cfg_parser.py`: 
  - Removed `__version__` information from class `IniParser`.
  - Changed to version management using `__version__` in `__init__.py`.
  - Added def items().
  - Fixed the return specification. class SectionProxy def items()
  - Fixed the return specification. class SectionProxy def keys()
- `tests/test_ini_parser.py`: 
  - Added def test_def_items().
  - Added def test_def_keys().

## [v0.1.1] - 2025-06-17
### Changed
- `README.md`: Fixed a typo in Operation Mode

## [v0.1.0] - 2025-06-17
### Added
- Initial commit for public release
