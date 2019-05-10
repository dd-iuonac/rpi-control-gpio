# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'digital_input.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_DigitalInput(object):
    def setupUi(self, DigitalInput):
        DigitalInput.setObjectName("DigitalInput")
        DigitalInput.resize(315, 49)
        self.verticalLayout = QtWidgets.QVBoxLayout(DigitalInput)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(DigitalInput)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_value = QtWidgets.QLineEdit(DigitalInput)
        self.lineEdit_value.setEnabled(False)
        self.lineEdit_value.setObjectName("lineEdit_value")
        self.horizontalLayout.addWidget(self.lineEdit_value)
        self.pushButton_read = QtWidgets.QPushButton(DigitalInput)
        self.pushButton_read.setObjectName("pushButton_read")
        self.horizontalLayout.addWidget(self.pushButton_read)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DigitalInput)
        QtCore.QMetaObject.connectSlotsByName(DigitalInput)

    def retranslateUi(self, DigitalInput):
        _translate = QtCore.QCoreApplication.translate
        DigitalInput.setWindowTitle(_translate("DigitalInput", "Form"))
        self.label.setText(_translate("DigitalInput", "Value:"))
        self.pushButton_read.setText(_translate("DigitalInput", "Read"))
