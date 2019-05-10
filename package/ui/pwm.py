# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pwm.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(290, 119)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.slider_frequency = QtWidgets.QSlider(Form)
        self.slider_frequency.setMaximum(9999)
        self.slider_frequency.setOrientation(QtCore.Qt.Horizontal)
        self.slider_frequency.setObjectName("slider_frequency")
        self.horizontalLayout.addWidget(self.slider_frequency)
        self.spinbox_frequency = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_frequency.setMaximum(9999.99)
        self.spinbox_frequency.setObjectName("spinbox_frequency")
        self.horizontalLayout.addWidget(self.spinbox_frequency)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.slider_duty_cycle = QtWidgets.QSlider(Form)
        self.slider_duty_cycle.setMaximum(100)
        self.slider_duty_cycle.setOrientation(QtCore.Qt.Horizontal)
        self.slider_duty_cycle.setObjectName("slider_duty_cycle")
        self.horizontalLayout_2.addWidget(self.slider_duty_cycle)
        self.spinbox_duty_cycle = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_duty_cycle.setMaximum(100.0)
        self.spinbox_duty_cycle.setObjectName("spinbox_duty_cycle")
        self.horizontalLayout_2.addWidget(self.spinbox_duty_cycle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.button_pwm = QtWidgets.QPushButton(Form)
        self.button_pwm.setCheckable(True)
        self.button_pwm.setObjectName("button_pwm")
        self.horizontalLayout_3.addWidget(self.button_pwm)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Frequency"))
        self.label_2.setText(_translate("Form", "Duty Cycle"))
        self.button_pwm.setText(_translate("Form", "Start"))
