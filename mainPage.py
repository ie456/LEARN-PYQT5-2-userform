
import sys
#from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from testForm import *
from dataTable import *


class MyMainWindow (QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openfile_New)
        self.pushButton_2.clicked.connect(self.openfile_Old)
        #self.pushButton_3.clicked.connect(self.openLoadWindow)
        #self.pushButton_3.clicked.connect(self.openWindow2)
        self.pushButton_4.clicked.connect(self.opentableview)





    def openfile_New(self):
        fileName1, _ = QFileDialog.getOpenFileName(self, "Select file", "./",
                                                   "Bom file(*.txt *.csv *.xlsx *.xlsm *.xls);; \
                                                   Text Files (*.txt);; \
                                    Excel file (*.csv *.xlsx *.xlsm *.xls)")
        self.lineEdit.setText(fileName1)


    def openfile_Old(self):
        fileName1, _ = QFileDialog.getOpenFileName(self, "Select file", "./",
                                                   "Bom file(*.txt *.csv *.xlsx *.xlsm *.xls);; \
                                                   Text Files (*.txt);; \
                                    Excel file (*.csv *.xlsx *.xlsm *.xls)")
        self.lineEdit_2.setText(fileName1)

    def opentableview(self):
        self.newDialog = subWindow()
        self.newDialog.show()

    def openWindow2(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=MyWindow_2()
        self.ui.setupUi(self.window)
        self.window.show()



class subWindow (QMainWindow,Ui_Form):
    def __init__(self,parent=None):
        super(subWindow,self).__init__(parent)
        self.setupUi(self)




if __name__=="__main__":
    app = QApplication(sys.argv)
    #app.setStyle('Windows')
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())