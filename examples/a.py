# coding: utf-8
import os
import sys
import configparser
from typing import List, Dict

OK_VAL = 0
NG_VAL = 1

try:
    import ini_parser as ini
except ImportError as e:
    msg = f"The 'ini_parser' module is required but not installed.\n"
    msg += f"You can install it with: pip install ini_parser-x.x.x-py3-none-any.whl\n"
    msg += f"Details: {e}"
    print(msg)
    raise SystemExit(NG_VAL)

SCR_PATH = os.path.abspath(sys.argv[0])

def main():
    # Defines the ini file name.
    ini_file = "hogehoge.ini"
    # Defines the character code encoding.
    encoding = "utf8"
    # Set DieMode information for IniParser
    ini.IniParser.mode = ini.DieMode.nException
    # Create default dict variable
    default_ini = get_ini_dict_val()
    # Check that a default value dict variable is of the expected type.
    if(ini.IniParser.is_valid_ini_dict(default_ini) == False):
        msg = f"def {sys._getframe().f_code.co_name}()\n"
        msg += f"Error detect. The type of the variable default_ini is invalid. type is not 'ini.IniDict'\n"
        msg += f"Check the type of the dict variable default_ini."
        die_print(msg)

    try:
        ini_parser = ini.IniParser(ini_file, default_ini, encoding)
    except ini.IniParserError as e:
        die_print(e)
    
    for section_name in ini_parser.sections():
        print(f"section={section_name}")
        for key,val in ini_parser[section_name].items():
            print(f"section={section_name},key={key},val={val}")

    val = ini_parser['Callback'].get('backup')
    print(f"backup={val},type={type(val)}")
    val = ini_parser['Callback'].get('zip')
    print(f"zip={val},type={type(val)}")
    val = ini_parser['Callback'].get('ext')
    print(f"ext={val},type={type(val)}")

    # Set the flag to 'True' to use the defined default value if information cannot be obtained.
    ini.IniParser.use_def_val = True
    # Change the default value to "False" if the information cannot be retrieved
    ini.IniParser.fallback_def_val = False

    # Create default dict variable
    default_ini2 = get_ini_dict_val2()
    # Defines the ini file name.
    ini_file2 = "hogehoge2.ini"
    try:
        ini_parser2 = ini.IniParser(ini_file2, default_ini2, encoding)
    except ini.IniParserError as e:
        die_print(e)

    for section_name in ini_parser2.sections():
        print(f"section={section_name}")
        for key, val in ini_parser2[section_name].items():
            print(f"section={section_name} ,key={key},val={val} ,type={type(val)}")

    # Enable debug mode. loglevel=2
    #ini.IniParser.set_debug_mode(2)
    print(f"----")
    for idx, str_section in enumerate(['user1', 'user2', 'user3']):
        id = ini_parser2.get(str_section,'id')
        pwd = ini_parser2.get(str_section,'password')
        host = ini_parser2.get(str_section,'host')
        print(f"num={idx},user={str_section},id={id},password={pwd},host={host}")

    print(f"--------")
    for idx, str_section in enumerate(['user1', 'user2', 'user3']):
        id = ini_parser2[str_section].get('id')
        pwd = ini_parser2[str_section].get('password')
        host = ini_parser2[str_section].get('host')
        print(f"num={idx},user={str_section},id={id},password={pwd},host={host}")

    str_section = 'user4'
    id = ini_parser2.get(str_section,'id')
    pwd = ini_parser2.get(str_section,'password')
    host = ini_parser2.get(str_section,'host')
    print(f"user={str_section},id={id},password={pwd},host={host}")

    ini.IniParser.use_def_val = False
    ini.IniParser.fallback_def_val = "2004/03/04"
    str_section = 'user3'
    birthday = ini_parser2.get(str_section,'birthday',fallback="1970年3月15日")
    print(f"user={str_section},birthday={birthday}")

    ini.IniParser.use_def_val = True
    ini.IniParser.fallback_def_val = "2004/03/04"
    str_section = 'user3'
    birthday = ini_parser2.get(str_section,'birthday')
    print(f"user={str_section},birthday={birthday}")

    ini.IniParser.use_def_val = True
    ini.IniParser.fallback_def_val = "2004/03/04"
    str_section = 'user3'
    birthday = ini_parser2.get(str_section,'birthday',fallback="1970/01/01")
    print(f"user={str_section},birthday={birthday}")
    # Debug mode disabled（DEBUG = 0）(Default)
    ini.IniParser.set_debug_mode(0)

    # Message examples

    # Set die_print() message output destination to "standard output" (Default)
    ini.IniParser.set_dieprint_output("stdout")
    # Set die_print() message output destination to "standard error"
    #ini.IniParser.set_dieprint_output("stderr")

    # Debug mode disabled（DEBUG = 0）(Default)
    #ini.IniParser.set_debug_mode(0)
    # Enable debug mode. loglevel=2
    ini.IniParser.set_debug_mode(2)

    # Set die_print() message output destination to "standard output" (Default)
    #ini.IniParser.set_debug_output("stdout")
    # Set debug output destination to ""standard error"
    #ini.IniParser.set_debug_output("stderr")

    # Debug message output (DEBUG level 2 messages)
    ini.IniParser.debug_print("This is a debug level 2 message.", level=2)

    # DEBUG level 3 is not displayed because it is higher than the current setting (2).
    ini.IniParser.debug_print("This should not be displayed at debug level 3.", level=3)

    #  Set die_print() message output destination to "standard output" (Default)
    ini.IniParser.set_debug_output("stdout")

    # Debug mode disabled（DEBUG = 0）(Default)
    ini.IniParser.set_debug_mode(0)

def get_ini_dict_val() -> ini.IniDict:
    '''
    ini fileのsection="DEFAULT"に設定したい情報をdict形式で設定
    '''
    return {
        'Callback': {
            'backup': {'type': bool, 'inf': False},
            'zip': {'type': bool, 'inf': False},
            'repall': {'type': bool, 'inf': False},
            'original': {'type': bool, 'inf': False},
            'ignorecase': {'type': bool, 'inf': False},
            'multiline': {'type': bool, 'inf': False},
            'dotall': {'type': bool, 'inf': False},
            'fullmatch': {'type': bool, 'inf': False},
            'notregex': {'type': bool, 'inf': False},
            'ext': {'type': List[str], 'inf': ['.txt', '.py' , '.pl', '.vhd', '.c']},
            'resultdir': {'type': str, 'inf': 'Result'},
            'in_file': {'type': str, 'inf': 'hoge.bat'},
            'int_list': {'type': List[int], 'inf': [100 ,99 ,73]},
            'bool_iist': {'type': List[bool], 'inf': [True ,False ,False,False]},
            'float_iist': {'type': List[float], 'inf': [123.4 ,234.5 ,3.14]},
        }
    }

def get_ini_dict_val2() -> ini.IniDict:
    '''
    ini fileのsection="DEFAULT"に設定したい情報をdict形式で設定
    '''
    return {
        'user1': {
            'host': {'type': str, 'inf': '172.31.2.100'},
            'id': {'type': str, 'inf': 'user1'},
            'password': {'type': str, 'inf': 'hogehoge1'},
        },
        'user2': {
            'id': {'type': str, 'inf': 'user2'},
            'password': {'type': str, 'inf': 'hogehoge2'},
        },
        'user3': {
            'id': {'type': str, 'inf': 'user3'},
            'password': {'type': str, 'inf': 'hogehoge3'},
        },
    }


def die_print(msg: str) -> None:
    print(msg)
    sys.exit(NG_VAL)

if __name__ == "__main__":
    main()
