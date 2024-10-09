from TP1 import TP1_1
import Utils

if __name__ == '__main__':
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
                print("Celsius to Fahrenheit")
                temperature = TP1_1.Temperature.new(Utils.take_temp())
                fahrenheit = temperature.convert_temperature(TP1_1.Temperature.Unit.Celsius)
                print(f"{Utils.set_precision(fahrenheit)}°F")
                break
            case 2:
                print("Fahrenheit to Celsius")
                temperature = TP1_1.Temperature.new(Utils.take_temp())
                celsius = temperature.convert_temperature(TP1_1.Temperature.Unit.Fahrenheit)
                print(f"{Utils.set_precision(celsius)}°C")
                break

