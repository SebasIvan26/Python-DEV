import sys
import os
from cx_Freeze import setup, Executable

#ADD FILES
files = {'include_files':['icon.ico','fonts/','icons/'], 'packages':["os"]}

#TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

#SETUP CX FREEZE
setup(  name = "GA Lab",
        version = "0.1",
        description = "Report automation tool",
        author = "Sebastien St Vil",
        options = {'build_exe': files},
        executables = [target]
    )