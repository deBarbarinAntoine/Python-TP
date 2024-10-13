import Utils
from TP1 import TP1_1
from Utils.Classes import MenuCLI, Colors


def cli():
    menu = MenuCLI.new("Celsius to Fahrenheit", "Fahrenheit to Celsius", title='Temperature Converter')
    match menu.run():
        case 0:
            print("Bye!")
            exit(0)
        case 1:
            title = 'Celsius to Fahrenheit'
            unit = TP1_1.Temperature.Unit.Celsius
        case 2:
            title = 'Fahrenheit to Celsius'
            unit = TP1_1.Temperature.Unit.Fahrenheit
        case _:
            return
    print()
    print(f"{Colors.BOLD}{title}{Colors.END}")
    print('▔' * len(title))
    temperature = TP1_1.Temperature.new(Utils.take_temp())
    new_temp, converted_unit = temperature.convert(unit)
    print()
    print(f"{temperature.get()}{unit.value} is equal to {Utils.set_precision(new_temp)}{converted_unit.value}")
    print()
    Utils.return_menu()