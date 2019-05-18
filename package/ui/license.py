# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/license.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_License(object):
    def setupUi(self, License):
        License.setObjectName("License")
        License.resize(818, 653)
        self.verticalLayout = QtWidgets.QVBoxLayout(License)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtWidgets.QTextBrowser(License)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_close = QtWidgets.QPushButton(License)
        self.button_close.setObjectName("button_close")
        self.horizontalLayout.addWidget(self.button_close)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(License)
        QtCore.QMetaObject.connectSlotsByName(License)

    def retranslateUi(self, License):
        _translate = QtCore.QCoreApplication.translate
        License.setWindowTitle(_translate("License", "Form"))
        self.button_close.setText(_translate("License", "Close"))


