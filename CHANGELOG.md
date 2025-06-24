# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

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
