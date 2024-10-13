import Utils
from TP1 import TP1_3
from Utils.Classes import Colors


def cli():
    print(f"{Colors.BOLD}Welcome Message Generator{Colors.END}")
    print('▔' * 25)
    print()
    while True:
        print("Enter a list of names (separated by space):")
        names = Utils.get_list_capitalized("> ")
        greetings = TP1_3.assign_random_greeting(names)
        print()
        for greeting in greetings:
            print(greeting)
        print()
        while True:
            print("Do you want to continue? [Y/n]")
            res = input("> ")
            match res.upper():
                case "N":
                    return
                case _:
                    break