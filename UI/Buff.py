# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Buff.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BuffDialog(object):
    def setupUi(self, BuffDialog):
        BuffDialog.setObjectName("BuffDialog")
        BuffDialog.resize(642, 392)
        BuffDialog.setMinimumSize(QtCore.QSize(642, 392))
        BuffDialog.setMaximumSize(QtCore.QSize(642, 392))
        self.buttonBox = QtWidgets.QDialogButtonBox(BuffDialog)
        self.buttonBox.setGeometry(QtCore.QRect(240, 350, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget_skill = QtWidgets.QWidget(BuffDialog)
        self.widget_skill.setGeometry(QtCore.QRect(10, 10, 621, 71))
        self.widget_skill.setObjectName("widget_skill")
        self.widget_equipment = QtWidgets.QWidget(BuffDialog)
        self.widget_equipment.setGeometry(QtCore.QRect(10, 90, 621, 251))
        self.widget_equipment.setObjectName("widget_equipment")
        self.equipment_aider = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_aider.setGeometry(QtCore.QRect(140, 130, 51, 51))
        self.equipment_aider.setObjectName("equipment_aider")
        self.equipment_rings = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_rings.setGeometry(QtCore.QRect(200, 130, 51, 51))
        self.equipment_rings.setObjectName("equipment_rings")
        self.equipment_magicShone = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_magicShone.setGeometry(QtCore.QRect(200, 190, 51, 51))
        self.equipment_magicShone.setObjectName("equipment_magicShone")
        self.equipment_earring = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_earring.setGeometry(QtCore.QRect(140, 190, 51, 51))
        self.equipment_earring.setObjectName("equipment_earring")
        self.equipment_pants = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_pants.setGeometry(QtCore.QRect(20, 70, 51, 51))
        self.equipment_pants.setObjectName("equipment_pants")
        self.equipment_shoes = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_shoes.setGeometry(QtCore.QRect(20, 130, 51, 51))
        self.equipment_shoes.setObjectName("equipment_shoes")
        self.equipment_coat = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_coat.setGeometry(QtCore.QRect(80, 10, 51, 51))
        self.equipment_coat.setObjectName("equipment_coat")
        self.equipment_necklace = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_necklace.setGeometry(QtCore.QRect(200, 70, 51, 51))
        self.equipment_necklace.setObjectName("equipment_necklace")
        self.equipment_weapon = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_weapon.setGeometry(QtCore.QRect(140, 10, 51, 51))
        self.equipment_weapon.setObjectName("equipment_weapon")
        self.equipment_shoulder = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_shoulder.setGeometry(QtCore.QRect(20, 10, 51, 51))
        self.equipment_shoulder.setObjectName("equipment_shoulder")
        self.equipment_bracelet = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_bracelet.setGeometry(QtCore.QRect(140, 70, 51, 51))
        self.equipment_bracelet.setObjectName("equipment_bracelet")
        self.equipment_belt = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_belt.setGeometry(QtCore.QRect(80, 70, 51, 51))
        self.equipment_belt.setObjectName("equipment_belt")
        self.equipment_title = QtWidgets.QPushButton(self.widget_equipment)
        self.equipment_title.setGeometry(QtCore.QRect(200, 10, 51, 51))
        self.equipment_title.setObjectName("equipment_title")
        self.fashion_halo = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_halo.setGeometry(QtCore.QRect(280, 70, 51, 51))
        self.fashion_halo.setText("")
        self.fashion_halo.setObjectName("fashion_halo")
        self.fashion_chest = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_chest.setGeometry(QtCore.QRect(350, 70, 51, 51))
        self.fashion_chest.setText("")
        self.fashion_chest.setObjectName("fashion_chest")
        self.fashion_shoes = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_shoes.setGeometry(QtCore.QRect(470, 130, 51, 51))
        self.fashion_shoes.setText("")
        self.fashion_shoes.setObjectName("fashion_shoes")
        self.fashion_hat = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_hat.setGeometry(QtCore.QRect(410, 10, 51, 51))
        self.fashion_hat.setText("")
        self.fashion_hat.setObjectName("fashion_hat")
        self.fashion_pants = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_pants.setGeometry(QtCore.QRect(410, 130, 51, 51))
        self.fashion_pants.setText("")
        self.fashion_pants.setObjectName("fashion_pants")
        self.fashion_coat = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_coat.setGeometry(QtCore.QRect(410, 70, 51, 51))
        self.fashion_coat.setText("")
        self.fashion_coat.setObjectName("fashion_coat")
        self.fashion_weapon = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_weapon.setGeometry(QtCore.QRect(280, 10, 51, 51))
        self.fashion_weapon.setText("")
        self.fashion_weapon.setObjectName("fashion_weapon")
        self.fashion_head = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_head.setGeometry(QtCore.QRect(350, 10, 51, 51))
        self.fashion_head.setText("")
        self.fashion_head.setObjectName("fashion_head")
        self.fashion_face = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_face.setGeometry(QtCore.QRect(470, 10, 51, 51))
        self.fashion_face.setText("")
        self.fashion_face.setObjectName("fashion_face")
        self.fashion_skin = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_skin.setGeometry(QtCore.QRect(470, 70, 51, 51))
        self.fashion_skin.setText("")
        self.fashion_skin.setObjectName("fashion_skin")
        self.fashion_waist = QtWidgets.QPushButton(self.widget_equipment)
        self.fashion_waist.setGeometry(QtCore.QRect(350, 130, 51, 51))
        self.fashion_waist.setText("")
        self.fashion_waist.setObjectName("fashion_waist")
        self.pet_pet = QtWidgets.QPushButton(self.widget_equipment)
        self.pet_pet.setGeometry(QtCore.QRect(550, 10, 51, 51))
        self.pet_pet.setText("")
        self.pet_pet.setObjectName("pet_pet")
        self.line = QtWidgets.QFrame(self.widget_equipment)
        self.line.setGeometry(QtCore.QRect(260, 10, 16, 231))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.widget_equipment)
        self.line_3.setGeometry(QtCore.QRect(530, 10, 16, 231))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(BuffDialog)
        self.line_2.setGeometry(QtCore.QRect(10, 80, 621, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(BuffDialog)
        self.buttonBox.accepted.connect(BuffDialog.accept)
        self.buttonBox.rejected.connect(BuffDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BuffDialog)

    def retranslateUi(self, BuffDialog):
        _translate = QtCore.QCoreApplication.translate
        BuffDialog.setWindowTitle(_translate("BuffDialog", "Dialog"))
