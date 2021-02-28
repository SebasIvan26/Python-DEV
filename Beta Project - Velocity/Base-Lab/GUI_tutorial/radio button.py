import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Combo Boxes")
        self.setGeometry(50,50,500,500)
        self.UI()
        
    def UI(self):
        self.name = QLineEdit(self)
        self.name.move(150,50)
        self.name.setPlaceholderText("Enter your name")
        self.surname = QLineEdit(self)
        self.surname.move(150,80)
        self.surname.setPlaceholderText("Enter your surname")
        self.male = QRadioButton("Male",self)
        self.male.move(150, 110)
        self.female = QRadioButton("Female",self)
        self.female.move(200, 110)


        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()