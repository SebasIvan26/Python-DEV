import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt


font = QFont("Times", 14)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialogs")
        self.setGeometry(350,150,400,400)
        self.UI()
        
    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        filebutton = QPushButton("Open File")
        savebutton = QPushButton("Save File")
        fontButton = QPushButton('Change Font')
        colorButton = QPushButton("Change Color")
        fontButton.clicked.connect(self.changeFont)
        colorButton.clicked.connect(self.changeColor)

        
        filebutton.clicked.connect(self.openFile)
        savebutton.clicked.connect(self.saveFile)
        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(filebutton)
        hbox.addWidget(savebutton)
        hbox.addWidget(colorButton)
        hbox.addWidget(fontButton)
        hbox.addStretch()
        self.setLayout(vbox)

        self.show()

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.editor.setCurrentFont(font)
    
    def changeColor(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)
    
    def openFile(self):
        path = QFileDialog.getOpenFileName(self, "Open a file", "", "All Files(*);;*txt")
        filePath = path[0]
        print(filePath)

        ##########If you want to open file in editor
        
        #file = open(filePath,'r')
        #content = file.read()
        #self.editor.setText(content)
    
    def saveFile(self):
        path = QFileDialog.getSaveFileName(self, "Save a file", "", "Excel Files(*);;xlsx")
        savePath = path[0]
        print(savePath)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()
