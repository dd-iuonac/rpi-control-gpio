
class Pin(object):
    def __init__(self):
        self.id = 0
        self.name = ""
        self.type = "Input"
        self.mode = "Digital"
        self.frequency = 0
        self.duty_cycle = 0
        self.value = 0
        self.pwm_instance = None

    def set_data(self, column: int, value):
        if column == 0:
            self.name = value
        elif column == 1:
            self.type = value
        elif column == 2:
            self.mode = value
        elif column == 3:
            if value > 0:
                self.frequency = value
        elif column == 4:
            if value > 0:
                self.duty_cycle = value
        elif column == 5:
            self.value = value

    def data(self, column: int):
        if column == 0:
            return self.name
        elif column == 1:
            return self.type
        elif column == 2:
            return self.mode
        elif column == 3:
            return self.frequency
        elif column == 4:
            return self.duty_cycle
        elif column == 5:
            return self.value

    def __repr__(self):
        data = {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "mode": self.mode,
            "frequency": self.frequency,
            "duty_cycle": self.duty_cycle,
            "value": self.value
        }
        return data

    def load(self, config: dict):
        self.id = config["id"]
        self.name = config["name"]
        self.type = config["type"]
        self.mode = config["mode"]
        self.frequency = config["frequency"]
        self.duty_cycle = config["duty_cycle"]
        self.value = config["value"]
