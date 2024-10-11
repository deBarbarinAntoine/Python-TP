import sys


def take_input(msg):
    val = input(msg)
    return val

def take_float(msg):
    val = take_input(msg)
    try:
        return float(val)
    except ValueError as e:
        raise e

def take_temp():
    while True:
        try:
            val = take_float("Enter a temperature: ")
        except ValueError:
            print("Please enter a valid number")
            continue
        return val

def set_precision(val, precision = 2):
    return round(val, precision)

def return_menu():
    print("type [ENTER] to return")
    input()
    return

def trim_capitalize(arr):
    result = []
    for elem in arr:
        elem = elem.strip().title()
        if elem != "":
            result.append(elem)
    return result

def get_list_capitalized(msg):
    val = input(msg)
    return trim_capitalize(val.split(' '))

def get_csv_capitalized(var):
    names = var.split(',')
    return trim_capitalize(names)

def get_divisors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

def trim_min_max(arr, min = 0, max = sys.maxsize):
    result = []
    for elem in arr:
        if min < elem < max:
            result.append(elem)
    return result