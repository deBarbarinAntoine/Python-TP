import Utils
from TP1 import TP1_1


def cli():
    print("Welcome to the temperature converter!")
    print("#####################################")
    print()
    print("1/ Celsius to Fahrenheit")
    print("2/ Fahrenheit to Celsius")
    print("0/ Exit")
    while True:
        try:
            val = Utils.take_float("Choose an option: ")
        except ValueError:
            print("Please enter a valid number")
            continue
        match val:
            case 0:
                print("Bye!")
                exit(0)
            case 1:
                print()
                print("Celsius to Fahrenheit")
                print("---------------------")
                temperature = TP1_1.Temperature.new(Utils.take_temp())
                unit = TP1_1.Temperature.Unit.Celsius
                fahrenheit, converted_unit = temperature.convert(unit)
                print()
                print(f"{temperature.get()}{unit.value} is equal to {Utils.set_precision(fahrenheit)}{converted_unit.value}")
                print()
                Utils.return_menu()
                break
            case 2:
                print()
                print("Fahrenheit to Celsius")
                print("---------------------")
                temperature = TP1_1.Temperature.new(Utils.take_temp())
                unit = TP1_1.Temperature.Unit.Fahrenheit
                celsius, converted_unit = temperature.convert(unit)
                print()
                print(f"{temperature.get()}{unit.value} is equal to {Utils.set_precision(celsius)}{converted_unit.value}")
                print()
                Utils.return_menu()
                break