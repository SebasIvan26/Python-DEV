import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

font = QFont("Times", 12)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Spin Boxes")
        self.setGeometry(250,150,500,500)
        self.UI()
        
    def UI(self):
        self.spinbox = QSpinBox(self)
        self.spinbox.move(150,100)
        self.spinbox.setFont(font)
        #self.spinbox.setMinimum(25)
        #self.spinbox.setMaximum(120)
        self.spinbox.setRange(25, 110)
        #self.spinbox.setPrefix('$ ')
        self.spinbox.setSuffix(' Miles')
        self.spinbox.setSingleStep(5)
        #self.spinbox.valueChanged.connect(self.getValue)
        button = QPushButton('Send', self)
        button.move(150, 140)
        button.clicked.connect(self.getValue)
        self.show()
    
    def getValue(self):
        value = self.spinbox.value()
        print(value)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()
