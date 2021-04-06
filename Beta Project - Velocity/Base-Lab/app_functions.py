################################################################################
##
## BY: Sebastien St Vil
## PROJECT MADE WITH: Qt Designer and PyQt5
## V: 1.0.0
##
## This project can be used freely for all uses, any information in the visual
## interface (GUI) can be modified without any implication.
##
##
################################################################################

## ==> GUI FILE
import sys
import getpass 
import traceback
import logging
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
###############################
import STAT_AUM as aum
import STAT_REV as rev
import Cash_Flow_Files as cashflow
import getstatsCashFlow as getstatsCF
import web_comparator
import userlog
from main import *

class Functions(MainWindow):
    bucketSourcePath, bucketDestPath = r"", r""
    pdfPriorPath, pdfCurrentPath = r"", r""
    cashflowPath, cashflowDest = r"", r""
    AUM_REV = True ##TRUE:AUM <--------> FALSE: REV
    ACTIVATE_EIB = True ##TRUE:Generate EIB <--------> FALSE: No generation

    def chooseBucketSource(self):
        global bucketSourcePath
        try:
            path = QFileDialog.getOpenFileName(self, "Open Excel file", "", "Excel Files(*);;*xls")
            bucketSourcePath = path[0]
            self.ui.linebucketEdit.setPlaceholderText(bucketSourcePath)
        except Exception:
            print("Error, Please Try again here")

    def chooseBucketDest(self):
        global bucketDestPath
        try:
            path = QFileDialog.getSaveFileName(self, "Save Excel file", "", "Excel Files(*);;*xlsx")
            bucketDestPath = path[0]
        except Exception:
            print("Error, Please Try again")

    def runBucketReport(self):
        global AUM_REV
        global ACTIVATE_EIB
        AUM_REV = True if "AUM" in self.ui.bucketcomboBox.currentText().upper() else False
        ACTIVATE_EIB = True if self.ui.bucketEIBcheckBox.isChecked() == True else False
        try:
            if not bucketSourcePath or not bucketDestPath:
                QMessageBox.information(self, "Information", "Plese enter Prelim File")
            elif len(bucketSourcePath) == 0 or len(bucketDestPath) == 0:
                QMessageBox.information(self, "Information", "Plese enter valid file path")
                return
        except Exception:
            QMessageBox.information(self, "Information", "Plese enter Prelim File/Saving location")
            return
        
        if ACTIVATE_EIB:
            self.ui.plainTextEdit.insertPlainText("EIB auto-generation is activated.\n\n")
        else:
            self.ui.plainTextEdit.insertPlainText("EIB auto-generation is not activated.\n\n")

        try:
            if AUM_REV:
                aum.main(bucketSourcePath, bucketDestPath, ACTIVATE_EIB)
                self.ui.plainTextEdit.insertPlainText("Source file loaded...\n\n")            
                self.ui.plainTextEdit.insertPlainText("Numbers are being verified....\n\n")                     
                self.ui.plainTextEdit.insertPlainText("File is being generated......\n\n")            
                self.ui.plainTextEdit.insertPlainText("STAT AUM is successfully saved in the below file path:\n\n")
                self.ui.plainTextEdit.insertPlainText(bucketDestPath +'\n\n')            

            elif not AUM_REV:
                rev.main(bucketSourcePath, bucketDestPath, ACTIVATE_EIB)
                self.ui.plainTextEdit.insertPlainText("Source file loaded...\n\n")            
                self.ui.plainTextEdit.insertPlainText("Numbers are being verified....\n\n")                     
                self.ui.plainTextEdit.insertPlainText("File is being generated......\n\n")            
                self.ui.plainTextEdit.insertPlainText("STAT REV is successfully saved in the below file path:\n")  
                self.ui.plainTextEdit.insertPlainText(bucketDestPath +'\n\n')
        except Exception:
            print("Error detected.....")  

    def choosePriorPDF(self):
        global pdfPriorPath
        try:
            path = QFileDialog.getOpenFileName(self, "Open PDF file", "", "PDF Files(*);;*PDF")
            pdfPriorPath = path[0]
            self.ui.lineEdit_10.setPlaceholderText(pdfPriorPath)
        except Exception:
            print("Error, Please Try again here")
    
    def chooseCurrentPDF(self):
        global pdfCurrentPath
        try:
            path = QFileDialog.getOpenFileName(self, "Open PDF file", "", "PDF Files(*);;*PDF")
            pdfCurrentPath = path[0]
            self.ui.lineEdit_11.setPlaceholderText(pdfCurrentPath)
        except Exception:
            print("Error, Please Try again here")

    def runComparator(self):
        global pdfPriorPath
        global pdfCurrentPath

        try:
            if not pdfPriorPath or not pdfCurrentPath:
                QMessageBox.information(self, "Information", "Plese enter Prelim File")
        except Exception:
            QMessageBox.information(self, "Information", "Plese enter Version 1/Version 2 for comparison")
            return

        try:
            QMessageBox.information(self, "Information", "Please wait, analyzing file......")
            QMessageBox.information(self, "Information", "ETA: 30s")
            web_comparator.main(pdfPriorPath, pdfCurrentPath)
        except Exception:
            return

    def chooseCashFlowSource(self):
        global cashflowPath
        try:
            path = QFileDialog.getOpenFileName(self, "Open Excel file", "", "Excel Files(*);;*xlsx")
            cashflowPath = path[0]
            self.ui.linecashflowtEdit_2.setPlaceholderText(cashflowPath)
        except Exception:
            print("Error, Please Try again here")
    
    def chooseCashFlowDest(self):
        global cashflowDest
        try:
            path = QFileDialog.getSaveFileName(self, "Save Excel file", "", "Excel Files(*);;*xlsx")
            cashflowDest = path[0]
        except Exception:
            print("Error, Please Try again")

    def generateCashFlowFile(self):
        global cashflowPath
        global cashflowDest

        try:
            if not cashflowPath or not cashflowDest:
                QMessageBox.information(self, "Information", "Plese enter WTC Cash Flow File")
            elif len(cashflowPath) == 0 or len(cashflowDest) == 0:
                QMessageBox.information(self, "Information", "Plese enter WTC Cash Flow File")
                return
        except Exception:
            QMessageBox.information(self, "Information", "Plese enter WTC Cash Flow File")
            return


        QMessageBox.information(self, "Information", "Please wait, analyzing file......")
        QMessageBox.information(self, "Remaining time", "ETA: 3 min")
        self.ui.cash_flow_plainTextEdit_2.insertPlainText("WTC Cash Flow file loaded...\n\n")            
        self.ui.cash_flow_plainTextEdit_2.insertPlainText("Numbers are being analyzed....\n\n")  
        cashflow.main(cashflowPath, cashflowDest)
        QMessageBox.information(self, "Information", "File is now generated")
        self.ui.cash_flow_plainTextEdit_2.insertPlainText("Please convert formulas to number values in order to obtain statistics\n\n")            
        self.ui.cash_flow_plainTextEdit_2.insertPlainText("Please run 'Get Statistics' to get Top Clients Cash Flow Stats \n")  

    
    def getCashFlowStats(self):
        global cashflowDest

        try:
            if not cashflowDest:
                QMessageBox.information(self, "Information", "Data for Statistics is not yet available, please generate Cash Flow file")
            elif len(cashflowPath) == 0 or len(cashflowDest) == 0:
                QMessageBox.information(self, "Information", "Data for Statistics is not yet available, please generate Cash Flow file")
                return
        except Exception:
            QMessageBox.information(self, "Information", "Data is not yet available, please generate Cash Flow file")
            return
        
        QMessageBox.information(self, "Information", "Please wait, getting statistics......")
        QMessageBox.information(self, "Remaining Time", "ETA: 5 min")
        getstatsCF.main(cashflowDest)
        self.ui.cash_flow_plainTextEdit_2.insertPlainText("Running Pandas libraries...\n\n")            
        self.ui.cash_flow_plainTextEdit_2.insertPlainText("extracting stats....\n\n")                               
        self.ui.cash_flow_plainTextEdit_2.insertPlainText("Top Clients Cashflow have been generated \n") 
        QMessageBox.information(self, "Information", "Top Clients Cashflow have been generated")

    def userLog(self):
        try:
            userlog.main()
        except Exception:
            return


        ######################## basic logger functionality##############################
log = logging.getLogger(__name__)
handler = logging.StreamHandler(stream=sys.stdout)
log.addHandler(handler)

def show_exception_box(log_msg):
    """Checks if a QApplication instance is available and shows a messagebox with the exception message. 
    If unavailable (non-console application), log an additional notice.
    """
    if QtWidgets.QApplication.instance() is not None:
            errorbox = QtWidgets.QMessageBox()
            errorbox.setText("Oops. An unexpected error occured:\n{0}".format(log_msg))
            errorbox.exec_()
    else:
        log.debug("No QApplication instance available.")
 
class UncaughtHook(QtCore.QObject):
    _exception_caught = QtCore.pyqtSignal(object)
 
    def __init__(self, *args, **kwargs):
        super(UncaughtHook, self).__init__(*args, **kwargs)

        # this registers the exception_hook() function as hook with the Python interpreter
        sys.excepthook = self.exception_hook

        # connect signal to execute the message box function always on main thread
        self._exception_caught.connect(show_exception_box)
 
    def exception_hook(self, exc_type, exc_value, exc_traceback):
        """Function handling uncaught exceptions.
        It is triggered each time an uncaught exception occurs. 
        """
        if issubclass(exc_type, KeyboardInterrupt):
            # ignore keyboard interrupt to support console applications
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
        else:
            exc_info = (exc_type, exc_value, exc_traceback)
            log_msg = '\n'.join([''.join(traceback.format_tb(exc_traceback)),
                                 '{0}: {1}'.format(exc_type.__name__, exc_value)])
            log.critical("Uncaught exception:\n {0}".format(log_msg), exc_info=exc_info)

            # trigger message box show
            self._exception_caught.emit(log_msg)
 
# create a global instance of our class to register the hook
qt_exception_hook = UncaughtHook()
        

    