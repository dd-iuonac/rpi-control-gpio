# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pulse_width_modulation.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_PulseWidthModulation(object):
    def setupUi(self, PulseWidthModulation):
        PulseWidthModulation.setObjectName("PulseWidthModulation")
        PulseWidthModulation.resize(290, 119)
        self.verticalLayout = QtWidgets.QVBoxLayout(PulseWidthModulation)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(PulseWidthModulation)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.slider_frequency = QtWidgets.QSlider(PulseWidthModulation)
        self.slider_frequency.setMaximum(9999)
        self.slider_frequency.setOrientation(QtCore.Qt.Horizontal)
        self.slider_frequency.setObjectName("slider_frequency")
        self.horizontalLayout.addWidget(self.slider_frequency)
        self.spinbox_frequency = QtWidgets.QDoubleSpinBox(PulseWidthModulation)
        self.spinbox_frequency.setMaximum(9999.99)
        self.spinbox_frequency.setObjectName("spinbox_frequency")
        self.horizontalLayout.addWidget(self.spinbox_frequency)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(PulseWidthModulation)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.slider_duty_cycle = QtWidgets.QSlider(PulseWidthModulation)
        self.slider_duty_cycle.setMaximum(100)
        self.slider_duty_cycle.setOrientation(QtCore.Qt.Horizontal)
        self.slider_duty_cycle.setObjectName("slider_duty_cycle")
        self.horizontalLayout_2.addWidget(self.slider_duty_cycle)
        self.spinbox_duty_cycle = QtWidgets.QDoubleSpinBox(PulseWidthModulation)
        self.spinbox_duty_cycle.setMaximum(100.0)
        self.spinbox_duty_cycle.setObjectName("spinbox_duty_cycle")
        self.horizontalLayout_2.addWidget(self.spinbox_duty_cycle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(PulseWidthModulation)
        QtCore.QMetaObject.connectSlotsByName(PulseWidthModulation)

    def retranslateUi(self, PulseWidthModulation):
        _translate = QtCore.QCoreApplication.translate
        PulseWidthModulation.setWindowTitle(_translate("PulseWidthModulation", "Form"))
        self.label.setText(_translate("PulseWidthModulation", "Frequency"))
        self.label_2.setText(_translate("PulseWidthModulation", "Duty Cycle"))
