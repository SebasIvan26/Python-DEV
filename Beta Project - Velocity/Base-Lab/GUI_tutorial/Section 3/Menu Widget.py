import sys
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt


font = QFont("Times", 14)
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(350,150,600,600)
        self.UI()
        
    def UI(self):
        ##################################Main Menu######################
        menubar = self.menuBar()
        files = menubar.addMenu("File")
        edits = menubar.addMenu("edit")
        view = menubar.addMenu("view")
        
        #statusbar = self.statusBar()
        #toolbar = self.toolBarArea(QToolBar("toolbar"))

        #######################Sub Menu Items##################
        new = QAction("Remove Project", self)
        new.setShortcut("Ctrl+0")
        files.addAction(new)
        new.setIcon((QIcon('/Users/sebastienstvil/Documents/Python/Python-DEV/GA Lab/GUI/Section 3/men_widget icns/folder.png')))
        new.triggered.connect(self.exitFunc)

        ###########################Toolbar########################
        tb = self.addToolBar("My Toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        newTb = QAction(QIcon("/Users/sebastienstvil/Documents/Python/Python-DEV/GA Lab/GUI/Section 3/icons/folder.png"), "New", self)
        tb.addAction(newTb)
        openTb = QAction(QIcon("/Users/sebastienstvil/Documents/Python/Python-DEV/GA Lab/GUI/Section 3/icons/empty.png"), "Open", self)
        tb.addAction(openTb)
        saveTb = QAction(QIcon("/Users/sebastienstvil/Documents/Python/Python-DEV/GA Lab/GUI/Section 3/icons/save.png"), "Save", self)
        tb.addAction(saveTb)
        exitTb = QAction(QIcon("/Users/sebastienstvil/Documents/Python/Python-DEV/GA Lab/GUI/Section 3/icons/exit.png"), "Exit", self)
        tb.addAction(exitTb)
        tb.actionTriggered.connect(self.btnFunc)
        self.combo = QComboBox()
        self.combo.addItems(["Spiderman", "Superman", "Batman"])
        tb.addWidget(self.combo)
        exitTb.triggered.connect(self.exitFunc)
        
        self.show()

    def btnFunc(self, btn):
        if btn.text() == "New":
            print("You clicked new Button")
        elif btn.text() == "Open":
            print("You clicked Open Button")
        else:
            print("You clicked save button")

    def exitFunc(self):
        mbox = QMessageBox.information(self, "Warning", "Are you sure ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()
    
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()
