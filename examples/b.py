import os
import sys
import ini_cfg_parser as ini
from typing import List

def main():
    encoding = "utf8"
    ini_file = "config.ini"
    ini.IniParser.set_die_mode(ini.DieMode.nException)
    default_ini = get_ini_dict_val()
    try:
        ini_parser = ini.IniParser(ini_file, default_ini, encoding)
    except ini.IniParserError as e:
        die_print(e)

    print(ini_parser.get('Callback', 'ext'))
    ini_parser.set('Callback', 'ext', ['.c', '.cpp' , '.c', '.h'])

    try:
        ini_parser = ini.IniParser(ini_file, default_ini, encoding)
    except ini.IniParserError as e:
        die_print(e)
    print(ini_parser.get('Callback', 'ext'))

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
        }
    }


if __name__ == "__main__":
    main()
