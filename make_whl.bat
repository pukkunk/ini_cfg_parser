if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
pip install build --no-binary :all:
python -m build
