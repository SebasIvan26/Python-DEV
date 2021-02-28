import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(10000,50, 300, 450)
        self.setWindowTitle('GA LAB test')

        self.show()



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())