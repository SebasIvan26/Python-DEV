import PyInstaller.__main__
####Run script to convert program to EXE
PyInstaller.__main__.run([
    'main.py',
    '--onedir',
    '--noconsole',
    '--icon=icon.ico'
])