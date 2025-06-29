# ini_parser.py

> This module is a utility that extends Python's built-in configparser module. It provides enhanced functionality for reading from and writing to INI files, including support for type conversion and default value interpolation.

## function
It can get and set configuration information in ini format.

This library is an enhanced parser for INI configuration files that allows you to define type information and default values in advance.
When a value is missing from the INI file, the parser automatically fills in the predefined default value.
Additionally, string values in the INI file are automatically converted to the specified types (e.g., int, bool, List[str], etc.) based on the provided type definitions.


Usage
```python
import ini_cfg_parser as ini
from typing import List

def get_ini_dict_val(section: str) -> ini.IniDict:
    return {
        section: {
            'lst_language': {'type': List[str], 'inf': ['English','Japanese','Russian','Korean']},
            'langage': {'type': int, 'inf': 0},
            'CygwinDirectory': {'type': str, 'inf': r'c:\uty\cygwin'},
            'ComPort': {'type': int, 'inf': 1},
            'lst_Parity': {'type': List[str], 'inf': ['even','odd','none','mark','space']},
            'parity': {'type': int, 'inf': 0},
            'DataBit': {'type': int, 'inf': 8},
            'StopBit': {'type': int, 'inf': 1},
        },
    }

encoding = "utf8"
ini_file = "config.ini"
section = 'setting1'
default_ini = get_ini_dict_val(section)
ini_parser = ini.IniParser(ini_file, default_ini, encoding)
lst_language = ini_parser.get(section, 'lst_language')
print(f"lst_language={lst_language},type={type(lst_language)}")
langage = ini_parser.get(section, 'langage')
print(f"langage={langage},type={type(langage)}")
print(f"langage setting={lst_language[langage]},type={type(lst_language[langage])}")
CygwinDirectory = ini_parser.get(section, 'CygwinDirectory')
print(f"CygwinDirectory={CygwinDirectory},type={type(CygwinDirectory)}")
ComPort = ini_parser.get(section, 'ComPort')
print(f"ComPort={ComPort},type={type(ComPort)}")
lst_Parity = ini_parser.get(section, 'lst_Parity')
print(f"lst_Parity={lst_Parity},type={type(lst_Parity)}")
parity = ini_parser.get(section, 'parity')
print(f"parity={parity},type={type(parity)}")
print(f"parity setting={lst_Parity[parity]},type={type(lst_Parity[parity])}")
DataBit = ini_parser.get(section, 'DataBit')
print(f"DataBit={DataBit},type={type(DataBit)}")
StopBit = ini_parser.get(section, 'StopBit')
print(f"StopBit={StopBit},type={type(StopBit)}")
```
If the ini file does not exist, the following config.ini will be created.
```cmd
# config.ini
[DEFAULT]
lst_language = English,Japanese,Russian,Korean
langage = 0
cygwindirectory = c:\uty\cygwin
comport = 1
lst_parity = even,odd,none,mark,space
parity = 0
databit = 8
stopbit = 1

[setting1]
lst_language = English,Japanese,Russian,Korean
langage = 0
cygwindirectory = c:\uty\cygwin
comport = 1
lst_parity = even,odd,none,mark,space
parity = 0
databit = 8
stopbit = 1
```
The result of executing the above script.
```cmd
lst_language=['English', 'Japanese', 'Russian', 'Korean'],type=<class 'list'>
langage=0,type=<class 'int'>
langage setting=English,type=<class 'str'>
CygwinDirectory=c:\uty\cygwin,type=<class 'str'>
ComPort=1,type=<class 'int'>
lst_Parity=['even', 'odd', 'none', 'mark', 'space'],type=<class 'list'>
parity=0,type=<class 'int'>
parity setting=even,type=<class 'str'>
DataBit=8,type=<class 'int'>
StopBit=1,type=<class 'int'>
```

### overview
- The `ini_cfg_parser` instance is initialized with the parameter get_ini_dict_val of type IniDict.
- The get_ini_dict_val parameter is a user-defined dictionary structure that specifies default values ​​and their expected types.

```cmd
# @param[in]    ini_path        : Path information for the ini file.(type=str)
# @param[in]    get_ini_dict_val: This parameter is a user-defined dictionary structure that specifies default values ​​and their expected types.(type=IniDict)
# @param[in]    encoding        : The type of character code encoding.(type=str)
ini_parser = ini.IniParser(ini_path=ini_file, get_ini_dict_val=default_ini, encoding=encoding)
```

#### Section structure
```python
IniDict = Dict[str, Dict[str, IniItem]]
```

#### Type of each ini item
```python
class IniItem(TypedDict):
    type: IniType
    inf: IniValue
```

#### Defining a type alias
```python
IniType = Union[Type[str], Type[int], Type[float], Type[bool], Type[List[str]], Type[List[int]], Type[List[float]], Type[List[bool]]]
IniValue = Union[str, int, float, bool, List[str], List[int], List[float], List[bool]]
```

When an error occurs in this library, the function `die_print()` is used to display a message.

Operation Mode: There are four operation modes.

- `nSysExit`: Executes `sys.exit(1)` to terminate the script.
- `nTkInter`: Uses `tkinter` to display a message in a dialog. Then executes `sys.exit(1)` to terminate the script.
- `nException`: Raises exception `IniParserError`. The error message is passed as the error information of the exception.
- `nTkInterException`: Uses `tkinter` to display a message in a dialog and then raises the exception `IniParserError`.

Setting the Mode:
Use `set_die_mode()` to set the mode.

How to set it up:

```python
ini.IniParser.set_die_mode(ini.DieMode.nSysExit)
```

## license
MIT License

## author
pukkunk
