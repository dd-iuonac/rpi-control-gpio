import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from db import save_configuration, load_configuration
from package.controllers import MainWindow

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


# Application class extends QApplication from QtWidgets

class Application(QApplication):
    def __init__(self, args):
        super(Application, self).__init__(args)
        # Set some properties
        self.setApplicationName('Raspberry Pi - G.P.I.O Control')
        self.setApplicationVersion('0.1')
        self.icon = QIcon(os.getcwd() + "/icons/rpi.png")
        self.setWindowIcon(self.icon)

        # On exiting application save the configuration
        self.aboutToQuit.connect(save_configuration)

        # Load the configuration
        load_configuration()

        # Create and show the main window
        self.main_window = MainWindow()
        self.main_window.show()
