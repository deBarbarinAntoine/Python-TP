from enum import Enum

class Temperature:
    """Represents a temperature value with support for conversion between Celsius and Fahrenheit."""
    def __init__(self, val = 0.0):
        """
        Initializes a new Temperature object with the given value.
        :param val: the value of the temperature
        """
        self.val = val

    class Unit(Enum):
        """Enumeration representing temperature units."""
        Celsius = "°C"
        Fahrenheit = "°F"
        def str(self):
            """Returns the string representation of the unit."""
            return self.value

    def get(self):
        """
        Retrieves the current temperature value.
        :return: the current temperature value
        """
        return self.val

    @staticmethod
    def new(val = 0.0):
        """
        Creates a new Temperature object with the given value.
        :param val: the value of the temperature
        :return: the new temperature object
        """
        return Temperature(val)

    def celsius_to_fahrenheit(self):
        """
        Converts the temperature from Celsius to Fahrenheit.
        :return: the temperature in Fahrenheit
        """
        return self.val * 1.8 + 32

    def fahrenheit_to_celsius(self):
        """
        Converts the temperature from Fahrenheit to Celsius.
        :return: the temperature in Celsius
        """
        return (self.val - 32) * 5 / 9

    def convert(self, units: Unit):
        """
        Converts the temperature to the specified unit.
        :param units: the unit to convert the temperature from
        :return: the converted temperature and the corresponding unit
        :raises ValueError: if the specified unit is not supported.
        """
        match units:
            case self.Unit.Celsius:
                return self.celsius_to_fahrenheit(), self.Unit.Fahrenheit
            case self.Unit.Fahrenheit:
                return self.fahrenheit_to_celsius(), self.Unit.Celsius
            case _:
                raise ValueError(f'Unit {units} not supported')
