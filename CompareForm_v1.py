# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CompareForm_v1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 762)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 20, 901, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(270, 20, 411, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Compare A with B"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Test1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Test2"))
        self.label.setText(_translate("MainWindow", "to"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Test1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Test2"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

