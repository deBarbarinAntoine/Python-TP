from enum import Enum

class Temperature:
    def __init__(self, val = 0.0):
        self.val = val

    class Unit(Enum):
        Celsius = "CELSIUS"
        Fahrenheit = "FAHRENHEIT"

    @staticmethod
    def new(val = 0.0):
        return Temperature(val)

    def celsius_to_fahrenheit(self):
        return self.val * 1.8 + 32

    def fahrenheit_to_celsius(self):
        return (self.val - 32) * 5 / 9

    def convert_temperature(self, units: Unit):
        match units:
            case self.Unit.Celsius:
                return self.celsius_to_fahrenheit()
            case self.Unit.Fahrenheit:
                return self.fahrenheit_to_celsius()
