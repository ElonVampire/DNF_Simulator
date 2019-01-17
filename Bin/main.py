import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from UI.MainWindow import Ui_MainWindow
from UI.Role import Ui_Role
from Config import Config

class MWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MWindow, self).__init__()
        self.roles = []
        self.setupUi(self)
        self.retranslateUi(self)
        self.init_role()
        self.init_actions()

    def init_actions(self):
        self.tabWidget_roles.currentChanged['int'].connect(self.actition_addRole)

    def init_role(self):
        r = self.tabWidget_role0
        role = Ui_Role()
        role.setupUi(r)
        role.retranslateUi(r)
        self.tabWidget_roles.setTabText(self.tabWidget_roles.indexOf(self.tabWidget_role0), '角色1')
        self.roles.append(r)

    def actition_addRole(self):
        if self.tabWidget_roles.currentWidget() is self.tabWidget_add:
            r = QWidget()
            role = Ui_Role()
            role.setupUi(r)
            role.retranslateUi(r)
            self.roles.append(r)
            count = self.roles.__len__()
            self.tabWidget_roles.insertTab(count - 1, r, f'角色{count}')
            self.tabWidget_roles.setCurrentWidget(r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MWindow()
    print(Config.WorkDir)
    w.show()
    sys.exit(app.exec_())
