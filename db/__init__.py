import json

from package.data import Pin
import RPi.GPIO as GPIO

CONFIGURATION_FILE = "db/configuration.json"

PIN_LIST = []


def load_configuration(configuration_file=CONFIGURATION_FILE):
    """
        Load the pins configuration from 'configuration.json' and creates the pin's objects
    """
    for pin in PIN_LIST:
    	if pin.pwm_instance:
    		pin.pwm_instance.stop()
    	GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    with open(configuration_file, "r") as file:
        data = json.load(file)
        
        PIN_LIST.clear()
        for config in data:
            pin = Pin()
            pin.load(data[config])
            PIN_LIST.append(pin)
            if pin.id == 6:
            	print(pin.__str__())
            
            
            if pin.type.__eq__("Output"):
            	GPIO.setup(pin.id, GPIO.OUT)
            	if pin.mode.__eq__("Digital"):
            		pin.pwm_instance = None
            		GPIO.output(pin.id, pin.value)
            	else:
            		if pin.pwm_instance:
            			pin.pwm_instance.ChangeDutyCycle(pin.duty_cycle)
            			pin.pwm_instance.ChangeFrequency(pin.frequency)
            		else:
            			pin.pwm_instance = GPIO.PWM(pin.id, pin.duty_cycle)
            			pin.pwm_instance.ChangeDutyCycle(pin.duty_cycle)
            			pin.pwm_instance.ChangeFrequency(pin.frequency)
            else:
            	pin.pwm_instance = None
            	if pin.mode.__eq__("Digital"):
            		GPIO.setup(pin.id, GPIO.IN)
            		

    print("DB: Configuration file has been loaded successfully!")


def save_configuration(configuration_file=CONFIGURATION_FILE):
    """
        Save the pins configuration to 'configuration.json'
    """
    data = {}
    for pin in PIN_LIST:
        data[pin.id] = pin.__repr__()

    with open(configuration_file, "w+") as file:
        json.dump(data, file, indent=4, sort_keys=True)

    print("DB: Configuration file has been saved!")
