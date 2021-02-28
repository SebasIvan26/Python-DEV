import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Combo Boxes")
        self.setGeometry(50,50,500,500)
        self.UI()
        
    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(150,100)
        button = QPushButton('Save', self)
        button.move(150,130)
        button.clicked.connect(self.getValue)
        self.combo.addItem("2")
        self.combo.addItems(["C", "C#", "Python"])
        list1 = ['Batman', 'SUperman', 'Spiderman']
        for name in list1:
            self.combo.addItem(name)
        
        self.show()
    
    def getValue(self):
        value = self.combo.currentText()
        print(value)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()