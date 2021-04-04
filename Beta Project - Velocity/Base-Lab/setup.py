import sys
import os
from cx_Freeze import setup, Executable

#ADD FILES
files = ['icon.ico','fonts/','icons/']

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
        options = {'build_exe': {'include_files':files}},
        executables = [target]
    )