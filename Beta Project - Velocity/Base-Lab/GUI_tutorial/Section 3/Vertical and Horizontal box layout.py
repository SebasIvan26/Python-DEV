import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

font = QFont("Times", 14)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical and Horizontal Box layoutd ")
        self.setGeometry(250,150,350,350)
        self.UI()
        
    def UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()
        btn1 = QPushButton()
        btn2 = QPushButton()

        topLayout.setContentsMargins(100, 10, 20, 20) #param: left, top, right, bottom
        topLayout.addWidget(cbox)
        topLayout.addWidget(rbtn)
        topLayout.addWidget(combo)

        bottomLayout.setContentsMargins(150, 10, 150, 10)
        bottomLayout.addWidget(btn1)
        bottomLayout.addWidget(btn2)
        ####Important, always set a layout for your main window otherwise window will show up blank
        self.setLayout(mainLayout)

        self.show()
    
 

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()
