# ini_parser.py
English version → [README.ja.md](https://github.com/pukkunk/ini_cfg_parser/blob/main/README.md)

> このモジュールは、Python 標準の configparser モジュールを拡張したユーティリティです。INI ファイルの読み書きに関して、型変換やデフォルト値の自動補完などの機能を追加しています。

## 機能
INI 形式の設定情報を取得および設定できます。

このライブラリは、INI 設定ファイル用の拡張パーサーであり、あらかじめ型情報やデフォルト値を定義できます。  
INI ファイルに値が存在しない場合、事前定義されたデフォルト値が自動的に適用されます。  
さらに、INI ファイル内の文字列値は、指定された型定義に基づいて自動的に変換されます（例：int、bool、List[str] など）。

使用例
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
INI ファイルが存在しない場合  
次の config.ini が自動生成されます。
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
実行結果例
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

### 概要
- ini_cfg_parser インスタンスは、IniDict 型の get_ini_dict_val を引数に初期化されます。
- get_ini_dict_val は、デフォルト値とその型を指定するユーザー定義の辞書構造です。

```cmd
# @param[in]    ini_path        : iniファイルのパス情報 (type=str)
# @param[in]    get_ini_dict_val: デフォルト値と型情報を定義したユーザー辞書 (type=IniDict)
# @param[in]    encoding        : 文字コード (type=str)
ini_parser = ini.IniParser(ini_path=ini_file, get_ini_dict_val=default_ini, encoding=encoding)
```

#### セクション構造
```python
IniDict = Dict[str, Dict[str, IniItem]]
```

#### 各 ini 項目の型
```python
class IniItem(TypedDict):
    type: IniType
    inf: IniValue
```

#### 型エイリアス定義
```python
IniType = Union[Type[str], Type[int], Type[float], Type[bool], Type[List[str]], Type[List[int]], Type[List[float]], Type[List[bool]]]
IniValue = Union[str, int, float, bool, List[str], List[int], List[float], List[bool]]
```

エラーメッセージの出力  
このライブラリでは、エラー発生時に die_print() 関数でメッセージを表示します。

動作モード: 動作モードは 4 種類あります。

- `nSysExit`: Executes `sys.exit(1)` to terminate the script.
- `nTkInter`: Uses `tkinter` to display a message in a dialog. Then executes `sys.exit(1)` to terminate the script.
- `nException`: Raises exception `IniParserError`. The error message is passed as the error information of the exception.
- `nTkInterException`: Uses `tkinter` to display a message in a dialog and then raises the exception `IniParserError`.

設定方法:
set_die_mode() でモードを設定します。


```python
ini.IniParser.set_die_mode(ini.DieMode.nSysExit)
```

## 動作確認済み環境

| OS                    | Python Version   |
|----------------------|-----------------:|
| Windows 11 Pro (64-bit) | 3.8.10 (64-bit) |
| Windows 11 Pro (64-bit) | 3.8.10 (32-bit) |

## license
MIT License

## author
pukkunk
