import json

from package.data import Pin

CONFIGURATION_FILE = "db/configuration.json"

PIN_LIST = []


def load_configuration(configuration_file=CONFIGURATION_FILE):
    """
        Load the pins configuration from 'configuration.json' and creates the pin's objects
    """

    with open(configuration_file, "r") as file:
        data = json.load(file)

        for config in data:
            pin = Pin()
            pin.load(data[config])
            PIN_LIST.append(pin)

    print("DB: Configuration file has been loaded successfully!")


def save_configuration(configuration_file=CONFIGURATION_FILE):
    """
        Save the pins configuration to 'configuration.json'
    """
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

    with open(configuration_file, "w+") as file:
        json.dump(data, file, indent=4, sort_keys=True)

    print("DB: Configuration file has been saved!")
