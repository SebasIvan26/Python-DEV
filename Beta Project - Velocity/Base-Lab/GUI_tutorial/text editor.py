import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

font = QFont("Times", 14)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Text editor")
        self.setGeometry(250,150,500,500)
        self.UI()
        
    def UI(self):
        self.editor = QPlainTextEdit(self)
        self.editor.move(150,80)
        self.editor.setReadOnly(True)
        button = QPushButton('Send', self)
        button.move(330, 280)
        button.clicked.connect(self.getValue)

        self.show()

    
    def getValue(self):
        text = self.editor.toPlainText()
        print(text)
        self.editor.remo
    
 

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()
