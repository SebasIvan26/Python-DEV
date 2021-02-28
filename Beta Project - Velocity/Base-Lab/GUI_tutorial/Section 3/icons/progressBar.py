import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt

COUNT = 0

font = QFont("Times", 14)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Bar")
        self.setGeometry(350,150,400,400)
        self.UI()
    
    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.progressBar = QProgressBar()
        btnStart = QPushButton("Start")
        btnStop = QPushButton("Stop")
        btnStart.clicked.connect(self.timerStart)
        btnStop.clicked.connect(self.timerStop)
        
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.runProgressBar)

        vbox.addWidget(self.progressBar)
        vbox.addLayout(hbox)
        hbox.addWidget(btnStart)
        hbox.addWidget(btnStop)
        self.setLayout(vbox)
        self.show()
    
    def runProgressBar(self):
        global COUNT
        COUNT += 1
        print(COUNT)
        self.progressBar.setValue(COUNT)
        if COUNT == 100:
            self.timerStop()

    def timerStart(self):
        self.timer.start()

    def timerStop(self):
        self.timer.stop()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == "__main__":
    main()
