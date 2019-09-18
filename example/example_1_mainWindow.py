import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from example_1_form import Ui_MainWindow


class ChangeTabColor(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(ChangeTabColor, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.tabWidget.setTabsClosable(True)
        #str = "QTabBar::tab{background-color:rbg(255,255,255,0);}"
        str = "QTabBar::tab{background-color:rbg(255,255,255,0);}" + \
              "QTabBar::tab:selected{color:red;background-color:rbg(255,200,255);} "
        self.tabWidget.setStyleSheet(str)
        self.tabWidget.currentChanged.connect(self.slot_small_tab)
        #self.tabwidget.tabCloseRequested.connect(self.closeTab)
        #self.tabwidget.tabCloseRequested[int].connect(self.remove_tab)

    def slot_small_tab(self):
            if self.tabWidget.currentIndex() == 0:
                print('666')
            elif self.tabWidget.currentIndex() == 1:
                print('222')
            else:
                pass


    def closeTab(self, index):
            if self.tabWidget.count() > 1:
                self.tabWidget.widget(index).deleteLater()
                self.tabWidget.removeTab(index)
            elif self.tabWidget.count() == 1:
                self.tabWidget.removeTab(0)
                self.on_pb_new_clicked()
    #def remove_tab(self, index):
    #    if index:
    #        # 当前页数
    #        self.current_page = 0
    #        self.tabwidget.removeTab(index)




def ui_main():
    app = QApplication(sys.argv)
    w = ChangeTabColor()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    ui_main()
