# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 657)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget_roles = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_roles.setEnabled(True)
        self.tabWidget_roles.setToolTipDuration(-10)
        self.tabWidget_roles.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_roles.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_roles.setUsesScrollButtons(True)
        self.tabWidget_roles.setDocumentMode(False)
        self.tabWidget_roles.setTabsClosable(True)
        self.tabWidget_roles.setMovable(False)
        self.tabWidget_roles.setTabBarAutoHide(False)
        self.tabWidget_roles.setObjectName("tabWidget_roles")
        self.tabWidget_role0 = QtWidgets.QWidget()
        self.tabWidget_role0.setObjectName("tabWidget_role0")
        self.tabWidget_roles.addTab(self.tabWidget_role0, "")
        self.tabWidget_add = QtWidgets.QWidget()
        self.tabWidget_add.setEnabled(False)
        self.tabWidget_add.setObjectName("tabWidget_add")
        self.tabWidget_roles.addTab(self.tabWidget_add, "")
        self.gridLayout.addWidget(self.tabWidget_roles, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 26))
        self.menubar.setObjectName("menubar")
        self.files = QtWidgets.QMenu(self.menubar)
        self.files.setObjectName("files")
        self.tools = QtWidgets.QMenu(self.menubar)
        self.tools.setObjectName("tools")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setObjectName("action_save_as")
        self.actionquit = QtWidgets.QAction(MainWindow)
        self.actionquit.setObjectName("actionquit")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actionhelp_2 = QtWidgets.QAction(MainWindow)
        self.actionhelp_2.setObjectName("actionhelp_2")
        self.files.addAction(self.action_open)
        self.files.addSeparator()
        self.files.addAction(self.action_save)
        self.files.addAction(self.action_save_as)
        self.files.addSeparator()
        self.files.addAction(self.actionquit)
        self.tools.addAction(self.actionhelp)
        self.help.addAction(self.actionhelp_2)
        self.menubar.addAction(self.files.menuAction())
        self.menubar.addAction(self.tools.menuAction())
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_roles.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DNF伤害模拟器V1.0  -  by skander820"))
        self.tabWidget_roles.setTabText(self.tabWidget_roles.indexOf(self.tabWidget_add), _translate("MainWindow", "+"))
        self.files.setTitle(_translate("MainWindow", "文件"))
        self.tools.setTitle(_translate("MainWindow", "工具"))
        self.help.setTitle(_translate("MainWindow", "帮助"))
        self.action_open.setText(_translate("MainWindow", "打开"))
        self.action_save.setText(_translate("MainWindow", "保存"))
        self.action_save_as.setText(_translate("MainWindow", "另存为"))
        self.actionquit.setText(_translate("MainWindow", "quit"))
        self.actionhelp.setText(_translate("MainWindow", "help"))
        self.actionhelp_2.setText(_translate("MainWindow", "help"))

