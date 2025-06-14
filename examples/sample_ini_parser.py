# SPDX-License-Identifier: MIT
# Copyright (c) 2025 pukkun
# coding: utf-8

import os
import sys
import re
import configparser

OK_VAL = 0
NG_VAL = 1

try:
    import ini_cfg_parser as ini
except ImportError as e:
    msg = f"The 'ini_cfg_parser' module is required but not installed.\n"
    msg += f"You can install it with: pip install ini_cfg_parser-x.x.x-py3-none-any.whl\n"
    msg += f"Details: {e}"
    print(msg)
    raise SystemExit(NG_VAL)
from typing import List

SCR_PATH = os.path.abspath(sys.argv[0])

def main() -> None :
    encoding = "utf8"
    # iniファイル名取得
    ini_file = "config.ini"
    # IniParserのdef die_print()mode情報を設定。エラー発生時、ExceptionでIniParserErrorを発生させる。
    ini.IniParser.set_die_mode(ini.DieMode.nException)
    # 設定したいデフォルト値を関数get_ini_dict_val()で設定
    default_ini = get_ini_dict_val()
    # デフォルト値用のdict型変数default_iniが期待の型であるかチェックを実施。
    if(ini.IniParser.is_valid_ini_dict(default_ini) == False):
        msg = f"def {sys._getframe().f_code.co_name}()\n"
        msg += f"Error detect. The type of the variable default_ini is invalid. type is not 'ini.IniDict'\n"
        msg += f"Check the type of the dict variable default_ini."
        die_print(msg)

    # IniParser クラスのインスタンスを生成
    try:
        ini_parser = ini.IniParser(ini_file, default_ini, encoding)
    except ini.IniParserError as e:
        die_print(e)
    print(f"ini_parser type={ini_parser}")

    print("---- check ini setting")
    for section_name in ini_parser.sections():
        items = ini_parser[section_name]
        for key, val in ini_parser[section_name].items():
            print(f"section={section_name},key={key},val={val},type={type(val)}")

    print(ini_parser.sections())
    section_name = 'Callback'
    # 取得したini_parserの情報をprint
    if ini_parser.has_section(section_name):
        print(f"There is section. section={section_name}")

    key_name = 'backup'
    if ini_parser.has_option(section_name, key_name):
        print(f"There is option. section={section_name},key={key_name}")
    
    val1 = ini_parser[section_name]['zip']
    print(f"val1={val1},type={type(val1)}")
    val2 = ini_parser[section_name]['multiline']
    print(f"val2={val2},type={type(val2)}")
    lst_val3 = ini_parser[section_name].get('ext')
    print(f"lst_val3={lst_val3},type={type(lst_val3)}")

    for section_name in ini_parser.sections():
        for key, val in ini_parser[section_name].items():
            print(f"section={section_name},key={key},val={ini_parser.get(section_name, key)},type={type(ini_parser.get(section_name, key))}")

    # 指定したsection,keyの情報をprint
    section = 'Callback'
    key = 'backup'
    print(f"section={section},key={key},val={ini_parser.get(section, key)},type={type(ini_parser.get(section, key))}")
    # 指定したsection,keyに値を設定
    key = 'resultdir'
    ini_parser.set(section, key, 'Result2')
    print(f"section={section},key={key},val={ini_parser.get(section, key)},type={type(ini_parser.get(section, key))}")
    # 指定したsection,keyに値を設定
    key = 'ext'
    ini_parser.set(section, key, [".c",".h",".cpp"])
    print(f"section={section},key={key},val={ini_parser.get(section, key)},type={type(ini_parser.get(section, key))}")

    #別のiniファイルに対して処理を実施。
    ini_file2 = "sample.ini"
    default_ini2 = get_ini_dict_val2()
    if(ini.IniParser.is_valid_ini_dict(default_ini2) == False):
        msg = f"def {sys._getframe().f_code.co_name}()\n"
        msg += f"Error detect. The type of the variable default_ini2 is invalid. type is not 'ini.IniDict'\n"
        msg += f"Check the type of the dict variable default_ini2."
        die_print(msg)
    try:
        ini_parser2 = ini.IniParser(ini_file2, default_ini2, encoding)
    except ini.IniParserError as e:
        die_print(e)

    for section_name,items in default_ini2.items():
        for key,val in items.items():
            print(f"section={section_name},key={key},val={ini_parser2.get(section_name, key)},type={type(ini_parser2.get(section_name, key))}")
    section = 'opt_replace'
    key = 'opt_re'
    str_val = ini_parser2.get(section, key)
    print(f"opt_re={str_val}")
    try:
        opt_re = ini.IniParser.re_option_check(str_val)
    except ini.IniParserError as e:
        print(f"{e}")

    print(f"ini_file2 write permit={ini.IniParser.can_write(ini_file2)}")
    print(f"ini_file2 read permit={ini.IniParser.can_read(ini_file2)}")

    print(f"--------------------------")
    #別のiniファイルに対して処理を実施。
    ini_file3 = "sample2.ini"
    default_ini3 = get_ini_dict_val3()

    if(ini.IniParser.is_valid_ini_dict(default_ini3) == False):
        msg = f"def {sys._getframe().f_code.co_name}()\n"
        msg += f"Error detect. The type of the variable default_ini3 is invalid. type is not 'ini.IniDict'\n"
        msg += f"Check the type of the dict variable default_ini3."
        die_print(msg)
    try:
        ini_parser3 = ini.IniParser(ini_file3, default_ini3, encoding)
    except ini.IniParserError as e:
        die_print(e)

    print("-=-=-=-=")
    ini_parser3 = ini.IniParser(ini_file3, default_ini3, encoding)
    for section in ini_parser3.sections():
        #items = ini_parser3[section]
        for key,val in ini_parser3[section].items():
            print(f"key={key},val={val}")

    for section in ini_parser3.sections():
        for key in ['user', 'password', 'host']:
            print(f"section={section},key={key},val={ini_parser3.get(section, key)}")
    if 'DEFAULT' in ini_parser3.sections():
        print("has DEFAULT")
        for key, val in ini_parser3['DEFAULT'].items():
            print(f"section={section},key={key},val={val}")
    print("-=-=-=-=")


    section = 'Callback'
    key = 'ext'
    try:
        ini_parser.set(section, key, ["hoge"])
        print(f"section={section},key={key},val={ini_parser.get(section, key)},type={type(ini_parser.get(section, key))}")
    except ini.IniParserError as e:
        die_print(e)

    print(f"TypeError発生を期待")
    try:
        ini_parser.set(section, key, "hoge")
        print(f"section={section},key={key},val={ini_parser.get(section, key)},type={type(ini_parser.get(section, key))}")
    except ini.IniParserError as e:
        print(e)

    sys.exit(OK_VAL)

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

def get_ini_dict_val2() -> ini.IniDict:
    '''
    ini fileのsection="DEFAULT"に設定したい情報をdict形式で設定
    '''
    return {
        'opt_replace': {
            'str_search': {'type': str, 'inf': 'search word'},
            'str_replace': {'type': str, 'inf': 'replace word'},
            'opt_re': {'type': str, 'inf': 're.UNICODE | re.IGNORECASE | re.MULTILINE | re.DOTALL'},
        }
    }

def get_ini_dict_val3() -> ini.IniDict:
    '''
    ini fileのsection="DEFAULT"に設定したい情報をdict形式で設定
    '''
    return {
        "DEFAULT": {
            'user': {'type': str, 'inf': 'default'},
            'password': {'type': str, 'inf': 'defpasswd'},
            'host': {'type': str, 'inf': '172.31.2.99'},
        },
        'sandbox': {
            'user': {'type': str, 'inf': 'root'},
            'password': {'type': str, 'inf': 'hogeroot'},
            'host': {'type': str, 'inf': '192.168.0.23'},
        },
        'user1': {
            'user': {'type': str, 'inf': 'user1'},
            'password': {'type': str, 'inf': 'hogepass1'},
            'host': {'type': str, 'inf': '172.31.2.190'},
        },
        'user2': {
            'user': {'type': str, 'inf': 'user2'},
            'password': {'type': str, 'inf': 'hogepass2'},
            'host': {'type': str, 'inf': '172.31.2.191'},
        },
        'user3': {
            'user': {'type': str, 'inf': 'user3'},
            'password': {'type': str, 'inf': 'hogepass3'},
            'host': {'type': str, 'inf': '172.31.2.193'},
        },
        'user4': {
        },
    }

##
# @brief        関数dieの文字列表示後、sys.exit(1)を実施。メッセージ表示して以上終了せず、returnコード1で終了する。
# @param[in]    filename        : target file name [type str]
# @retval       none            : 
def die_print(msg):
    print(msg)
    sys.exit(NG_VAL)

if __name__ == "__main__":
    main()
