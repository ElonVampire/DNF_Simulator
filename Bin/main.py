import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from UI.MainWindow import Ui_MainWindow
from UI.Role import Ui_Role


class MWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MWindow, self).__init__()
        self.rolecount = 2
        self.setupUi(self)
        self.retranslateUi(self)
        self.init_role()
        self.init_actions()

    def init_actions(self):
        self.tabWidget_roles.tabBarClicked['int'].connect(self.actition_addRole)
        self.tabWidget_roles.tabCloseRequested.connect(self.close_Tab)
        self.tabWidget_roles.currentChanged['int'].connect(self.add_button_move)

    def close_Tab(self, index):
        if self.tabWidget_roles.count() > 1:
            if self.tabWidget_roles.indexOf(self.tabWidget_add) != index:
                self.tabWidget_roles.removeTab(index)
                self.tabWidget_roles.setCurrentIndex(index)
        else:
            self.close()

    def init_role(self):
        r = self.tabWidget_role0
        role = Ui_Role()
        role.setupUi(r)
        role.retranslateUi(r)
        self.tabWidget_roles.setTabText(self.tabWidget_roles.indexOf(self.tabWidget_role0), '角色1')
        self.tabWidget_roles.setCurrentWidget(self.tabWidget_role0)

    def add_button_move(self, index):
        if self.tabWidget_roles.currentWidget() is self.tabWidget_add:
            self.tabWidget_roles.setCurrentIndex(index-1)

    def actition_addRole(self, index):
        if index == self.tabWidget_roles.indexOf(self.tabWidget_add):
            r = QWidget()
            role = Ui_Role()
            role.setupUi(r)
            role.retranslateUi(r)
            self.tabWidget_roles.insertTab(index, r, f'角色{self.rolecount}')
            self.tabWidget_roles.setCurrentWidget(r)
            self.rolecount += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MWindow()
    w.show()
    sys.exit(app.exec_())
