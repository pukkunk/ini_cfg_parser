# tests/test_ini_parser.py

import ini_cfg_parser as ini

OK_VAL = 0
NG_VAL = 1

try:
    import pytest
except ImportError as e:
    msg = f"The 'ini_parser' module is required but not installed.\n"
    msg += f"You can install it with: pip install pytest\n"
    msg += f"Details: {e}"
    print(msg)
    raise SystemExit(NG_VAL)

def test_set_debug_output_stdout(capsys):
    ini.IniParser.set_debug_mode(1)
    ini.IniParser.set_debug_output("stdout")

    ini.IniParser.debug_print("hello world", level=1)
    captured = capsys.readouterr()  # 出力をキャプチャ
    assert "[DEBUG1] hello world" in captured.out  # stdoutにあるかチェック
    assert captured.err == ""  # stderrは空のはず

def test_set_debug_output_stderr(capsys):
    ini.IniParser.set_debug_mode(1)
    ini.IniParser.set_debug_output("stderr")

    ini.IniParser.debug_print("hello world", level=1)

    captured = capsys.readouterr()
    assert "[DEBUG1] hello world" in captured.err
    assert captured.out == ""

