import difflib
import subprocess
import os
import sys
import platform

system = platform.system()
dest = r'/Users/sebastienstvil/Documents/Python/Python-DEV/Beta Custom - GIT pulls copy/Base-master/Testing/pdf_Tests/diff.html' if system != 'Darwin' else 'Onedrive'
print(dest)