from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtCore, QtGui
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import (QMessageBox, QWidget, QMainWindow, QApplication, QTabWidget, QGridLayout, QLabel,
                             QLineEdit, QPushButton, QScrollArea, QVBoxLayout
, QTextEdit)
import sys, os


# reload(sys)
# sys.setdefaultencoding('utf-8')

class MyConsole(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
        self.parent = parent
        self.initUI()

        # 初始化UI

    def initUI(self):
        # 網格佈局
        self.gridlayout = QGridLayout()

        # 設定出20 x 20 的格局  ,目的是把固定空間 等分空間
        for i in range(20):
            self.gridlayout.setColumnStretch(i, 1)
            self.gridlayout.setRowStretch(i, 1)

        lb1 = QLabel(u'賬戶：')
        lb2 = QLabel(u'密碼：')
        self.userEntry = QLineEdit()
        self.passEntry = QLineEdit()
        self.passEntry.setEchoMode(QLineEdit.Password)  # 輸出型別為密碼型別
        self.loginBtn = QPushButton(u"登入")
        self.loginBtn.setFixedSize(40, 20)  # 與resize()類似，未找到不同點
        # self.connect(self.loginBtn, QtCore.SIGNAL('clicked()'), self.onLoginButton)
        self.loginBtn.clicked.connect(self.onLoginButton)

        self.gridlayout.addWidget(lb1, 0, 0)
        self.gridlayout.addWidget(lb2, 1, 0)
        self.gridlayout.addWidget(self.userEntry, 0, 1, 1, 3)
        self.gridlayout.addWidget(self.passEntry, 1, 1, 1, 3)
        self.gridlayout.addWidget(self.loginBtn, 0, 4, 1, 2)

        self.setLayout(self.gridlayout)

        # 點選登入按鈕

    def onLoginButton(self):
        # 獲取輸入內容
        username = self.userEntry.text()
        password = self.passEntry.text()
        try:
            QMessageBox.about(self, '提示', u"登入成功")
        except Exception as e:
            print(e)
        print(username + u'登入成功！\n' + u"密碼是：" + password + '\n------------------------')


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        # 定義Tab控制元件
        tabs = QTabWidget(self)

        # 第1個Tab頁
        # tab1 = QWidget()
        ''''' 
        #這是不帶滾動條的寫法   
        vbox = QVBoxLayout() 
        console = MyConsole(self) 
        vbox.addWidget(console) 
        tab1.setLayout(vbox) 
        '''
        # 這是帶滾動條的寫法
        console = MyConsole(self)  # 自定義物件，登入
        console.setMinimumSize(500, 350)
        # 滾動條
        scroll = QScrollArea()
        scroll.setWidget(console)
        # scroll.setAutoFillBackground(True)
        # scroll.setWidgetResizable(True)
        # vbox = QVBoxLayout()
        # vbox.addWidget(scroll)
        # tab1.setLayout(vbox) # QWidget，需要放到佈局中
        tab1 = scroll  # 這裡可以直接將滾動條作為tab頁內容

        # 第2個Tab頁
        self.tab2 = QTextEdit()

        # QTabWidget的2個Tab頁
        tabs.addTab(tab1, u"控制檯")
        tabs.addTab(self.tab2, u"日誌輸出")

        # QTabWidget的控制元件大小
        tabs.resize(400, 320)
        # 主窗體的大小
        self.resize(500, 350)

        # 禁止最大化
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.show()

        # 重定向輸出  （關鍵）
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)

        # 當物件被刪除時，會自動被呼叫

    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def normalOutputWritten(self, text):
        cursor = self.tab2.textCursor()  # 游標
        cursor.movePosition(QtGui.QTextCursor.End)  # 游標移至最後
        cursor.insertText(text)  # 插入文字
        self.tab2.setTextCursor(cursor)  # 使之生效
        self.tab2.ensureCursorVisible()  # 確保滾動文字編輯時游標是可視的。



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show
    sys.exit(app.exec_())
