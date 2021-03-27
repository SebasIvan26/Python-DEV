################################################################################
##
## BY: Sebastien St Vil
## PROJECT MADE WITH: Qt Designer and PyQt5
## V: 1.0.0
##
################################################################################

import sys
import getpass
import time
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from app_modules import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ## PRINT ==> SYSTEM
        
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        name = getpass.getuser()
        name_database = {'stvils': 'Seb', 'sebastienstvil': 'Seb', 'slittle': 'Scott', 'eguillen': 'Elzé', 'millens': 'Sarah'}
        if name in name_database:
            self.ui.label_welcome_usr.setText('Welcome,   ' + name_database[getpass.getuser()])
        else:
            self.ui.label_welcome_usr.setText('Welcome,   ' + getpass.getuser())

        
        clock2 = time.strftime("%b %d ")
        #clock = time.strftime(r"%b %d %Y %-I:%M %p")
        self.ui.label_time.setText(clock2)


        self.setWindowTitle('Main Window - GA Lab')
        UIFunctions.labelTitle(self, 'Main Window - GA Lab')
        UIFunctions.labelDescription(self, 'GA LAB')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        #UIFunctions.enableMaximumSize(self, 200, 100)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Bucket Report", "btn_bucket_report", "url(:/16x16/icons/16x16/cil-chart-line.png)", True)
        UIFunctions.addNewMenu(self, "Comparator", "btn_capital_calc", "url(:/16x16/icons/16x16/cil-browser.png)", True)
        UIFunctions.addNewMenu(self, "Cash Flow File", "btn_cash_flow", "url(:/16x16/icons/16x16/cil-double-quote-sans-right.png)", True)
        UIFunctions.addNewMenu(self, "Cash Finder", "btn_cash_finder", "url(:/16x16/icons/16x16/cil-justify-left.png)", False)
        ##self.ui.btn_toggle_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets))
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "GA", "", True)
        ## ==> END ##

#################################USER_INTERFACE FUNCTIONS##########################################
        self.ui.bucketpushButton.clicked.connect(lambda: Functions.chooseBucketSource(self))
        self.ui.bucketSaveButton.clicked.connect(lambda: Functions.chooseBucketDest(self))
        self.ui.bucketRunButton.clicked.connect(lambda: Functions.runBucketReport(self))

        self.ui.prior_pushButton_2.clicked.connect(lambda: Functions.choosePriorPDF(self))
        self.ui.current_pushButton.clicked.connect(lambda: Functions.chooseCurrentPDF(self))
        self.ui.webCompareButton.clicked.connect(lambda: Functions.runComparator(self))

        self.ui.cash_flow_pushButton_2.clicked.connect(lambda: Functions.chooseCashFlowSource(self))
        self.ui.cashflow_savebutton.clicked.connect(lambda: Functions.chooseCashFlowDest(self))
        self.ui.cash_flow_generate_button.clicked.connect(lambda: Functions.generateCashFlowFile(self))
        self.ui.cash_flow_getstats_button.clicked.connect(lambda: Functions.getCashFlowStats(self))



        
        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################



        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.cashTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_bucket_report":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_bucket_report")
            UIFunctions.labelPage(self, "Bucket Report")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_capital_calc":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_capitalcalc)
            UIFunctions.resetStyle(self, "btn_capital_calc")
            UIFunctions.labelPage(self, "Capital Calc tools")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        #WTC Cash FLow Page
        if btnWidget.objectName() == "btn_cash_flow":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_cash_flow_file)
            UIFunctions.resetStyle(self, "btn_cash_flow")
            UIFunctions.labelPage(self, "WTC Cash Flow Files")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        
        ######################Testing Functions#######################
        if btnWidget.objectName() == "btn_cash_finder":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_cash)
            UIFunctions.resetStyle(self, "btn_cash_finder")
            UIFunctions.labelPage(self, "Cash Finder")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

        try:
            clock = str(time.strftime("%b %d %Y %-I:%M %p"))
            self.ui.label_time.setText(clock)
        except Exception:
            print("error loading time")

        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
