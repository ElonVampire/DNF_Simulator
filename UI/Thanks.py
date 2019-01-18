# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Thanks.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Thanks(object):
    def setupUi(self, Thanks):
        Thanks.setObjectName("Thanks")
        Thanks.resize(626, 575)
        self.gridLayout = QtWidgets.QGridLayout(Thanks)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Thanks)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Thanks)
        QtCore.QMetaObject.connectSlotsByName(Thanks)

    def retranslateUi(self, Thanks):
        _translate = QtCore.QCoreApplication.translate
        Thanks.setWindowTitle(_translate("Thanks", "Form"))
        self.label.setText(_translate("Thanks", "感谢使用，再次点击关闭按钮退出"))

