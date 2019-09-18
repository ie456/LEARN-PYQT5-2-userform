# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataTable.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 579)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 561))
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)

        self.tabWidget.tabBar().setTabButton(0, self.tabWidget.tabBar().RightSide, None)

        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(0, 70, 771, 471))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)


        self.tabWidget.setCurrentIndex(1)
        self.tabWidget.tabCloseRequested['int'].connect(self.tabWidget.setCurrentIndex)
        self.tabWidget.tabCloseRequested['int'].connect(self.tabWidget.deleteLater)





        QtCore.QMetaObject.connectSlotsByName(Form)




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "+"))

