import difflib
import subprocess
import os
import platform
from tika import parser # pip install tika
from difflib import SequenceMatcher, HtmlDiff


def generateDiff(path1, path2):
    system = platform.system() ##Windows or MAC

    raw = parser.from_file(path1)
    raw2 = parser.from_file(path2)

    textPDF1 = raw['content'].strip().splitlines()
    textPDF2 = raw2['content'].strip().splitlines()


    delta = difflib.Differ().compare(textPDF1, textPDF2)
    print('\n'.join(delta))

    delta_html = HtmlDiff().make_file(textPDF1, textPDF2)

    dest = r'/Users/sebastienstvil/Documents/Python/Python-DEV/Beta Project - Velocity/Base-Lab/Testing/pdf_Tests/diff.html'\
         if system == 'Darwin' else r'\\prod-corpfile\netshare\GA\000-Common Files\Virtual - GA Lab\cache\diff.html'
    with open(dest,'w') as f:
        f.write(delta_html)

    ###OPEN USER WEBPAGE
    openBrowser(dest)
    
    

def openBrowser(link):
    try: # should work on Windows
        os.startfile(link)
    except AttributeError:
        try: # should work on MacOS and most linux versions
            subprocess.call(['open', link])
        except:
            print('Could not open URL')
            
    #seq = SequenceMatcher(a=textPDF1, b=textPDF2)
    #print(seq.ratio())

def main(path1, path2):

    generateDiff(path1, path2)


if __name__ == "__main__":
    main(pdfPath1, pdfPath2)
