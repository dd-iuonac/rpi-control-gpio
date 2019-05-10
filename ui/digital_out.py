# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'digital_out.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(415, 81)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.slider_value = QtWidgets.QSlider(Form)
        self.slider_value.setMaximum(1)
        self.slider_value.setPageStep(1)
        self.slider_value.setOrientation(QtCore.Qt.Horizontal)
        self.slider_value.setObjectName("slider_value")
        self.horizontalLayout.addWidget(self.slider_value)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinbox_value = QtWidgets.QSpinBox(Form)
        self.spinbox_value.setMaximum(1)
        self.spinbox_value.setObjectName("spinbox_value")
        self.horizontalLayout.addWidget(self.spinbox_value)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Low"))
        self.label_2.setText(_translate("Form", "High"))


