from PyQt5.QtWidgets import QApplication

from db import save_configuration, load_configuration
from package.controllers import MainWindow


# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)


class Application(QApplication):
    def __init__(self, args):
        super(Application, self).__init__(args)
        self.setApplicationName('Raspberry Pi - G.P.I.O Control')
        self.setApplicationVersion('0.1')
        self.aboutToQuit.connect(save_configuration)

        # Load the configuration
        load_configuration()

        self.main_window = MainWindow()
        self.main_window.show()
