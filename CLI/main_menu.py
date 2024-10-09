import Utils
from CLI import TP1_1, TP1_2, TP1_3


def cli():
    print("###############################")
    print("Welcome to Antoine's Python TP!")
    print("###############################")
    while True:
        print("#######    Main Menu    #######")
        print()
        print("1/ TP1.1 Temperature Converter")
        print("2/ TP1.2 Sum and Product of Even Numbers")
        print("3/ TP1.3 Welcome Message Generator")
        print("4/ TP1.4 Mental Arithmetic")
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
                    TP1_1.cli()
                    break
                case 2:
                    TP1_2.cli()
                    break
                case 3:
                    TP1_3.cli()
                    break