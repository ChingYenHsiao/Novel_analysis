# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\docx_color_seperate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Docx_color_seperate(object):
    def setupUi(self, Docx_color_seperate):
        Docx_color_seperate.setObjectName("Docx_color_seperate")
        Docx_color_seperate.resize(1207, 175)
        self.buttonBox = QtWidgets.QDialogButtonBox(Docx_color_seperate)
        self.buttonBox.setGeometry(QtCore.QRect(290, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Docx_color_seperate)
        self.pushButton.setGeometry(QtCore.QRect(70, 50, 231, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Docx_color_seperate)
        self.lineEdit.setGeometry(QtCore.QRect(370, 50, 751, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Docx_color_seperate)
        self.buttonBox.accepted.connect(Docx_color_seperate.accept)
        self.buttonBox.rejected.connect(Docx_color_seperate.reject)
        QtCore.QMetaObject.connectSlotsByName(Docx_color_seperate)

    def retranslateUi(self, Docx_color_seperate):
        _translate = QtCore.QCoreApplication.translate
        Docx_color_seperate.setWindowTitle(_translate("Docx_color_seperate", "Dialog"))
        self.pushButton.setText(_translate("Docx_color_seperate", "Select docx file"))

