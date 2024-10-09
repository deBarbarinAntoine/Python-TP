import Utils
from TP1 import TP1_2

def cli():
    print("Sum and Product of Even Numbers")
    print("###############################")
    print()
    while True:
        val = input("Enter a number: ")
        try:
            val = int(val)
        except ValueError:
            print("Please enter a valid integer")
            continue
        try:
            even_numbers = TP1_2.get_even_numbers(val)
        except ValueError as e:
            print(e)
            continue
        print()
        print(f"1/ {TP1_2.get_expression(even_numbers, '+')} = {TP1_2.sum_list(even_numbers)}")
        print(f"2/ {TP1_2.sum_list(even_numbers)} = {TP1_2.get_expression(even_numbers, '+')}")
        print(f"3/ {TP1_2.get_expression(even_numbers, 'x')} = {TP1_2.product_list(even_numbers)}")
        print(f"4/ {TP1_2.product_list(even_numbers)} = {TP1_2.get_expression(even_numbers, 'x')}")
        print()
        while True:
            print("Do you want to continue? [Y/n]")
            res = input("> ")
            match res.upper():
                case "N":
                    return
                case _:
                    break
