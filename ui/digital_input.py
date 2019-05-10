# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'digital_input.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(315, 49)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_value = QtWidgets.QLineEdit(Form)
        self.lineEdit_value.setEnabled(False)
        self.lineEdit_value.setObjectName("lineEdit_value")
        self.horizontalLayout.addWidget(self.lineEdit_value)
        self.pushButton_read = QtWidgets.QPushButton(Form)
        self.pushButton_read.setObjectName("pushButton_read")
        self.horizontalLayout.addWidget(self.pushButton_read)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Value:"))
        self.pushButton_read.setText(_translate("Form", "Read"))


