import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

font = QFont("Times", 14)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Timer")
        self.setGeometry(250,150,350,350)
        self.UI()
        
    def UI(self):
        vbox = QVBoxLayout()
        button1 = QPushButton("Save")
        button2 = QPushButton("Exit")
        button3 = QPushButton("Hello")
        vbox.addStretch()  #Moves button close to one another 
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        vbox.addStretch()
        self.setLayout(vbox)
        self.show()
    
 

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()
