import json
import sys

import RPi.GPIO as GPIO

from PyQt5.QtWidgets import QApplication

from controllers import MainWindow
from data import Pin


"""
Save the current pins configuration
"""


def save_configuration():
    data = {}
    for pin in PIN_LIST:
        config = {
            "id": pin.id,
            "name": pin.name,
            "type": pin.type,
            "mode": pin.mode,
            "frequency": pin.frequency,
            "duty_cycle": pin.duty_cycle,
            "value": pin.value
        }
        data[pin.id] = config

    with open("configuration.json", "w+") as file:
        json.dump(data, file, indent=4, sort_keys=True)


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    """
    Load the pins configuration from 'configuration.json'
    """
    PIN_LIST = []
    with open("configuration.json", "r") as file:
        data = json.load(file)
             
        for config in data:
            pin = Pin()
            pin.load(data[config])
            PIN_LIST.append(pin)

    """
    Create and run the QApplication
    """
    application = QApplication(sys.argv)
    application.aboutToQuit.connect(save_configuration)
    main_window = MainWindow(PIN_LIST)
    main_window.show()
    sys.exit(application.exec_())


