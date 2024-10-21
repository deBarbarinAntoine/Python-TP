import sys


def set_precision(val, precision = 2):
    """
    Rounds the given value to the given precision.
    :param val: a float value
    :param precision: the number of digits to round to
    :return: the rounded value
    """
    return round(val, precision)

def trim_capitalize(arr):
    """
    Trims and capitalizes every entry of the given array.
    :param arr: a string array
    :return: the array of trimmed and capitalized strings
    """
    result = []
    for elem in arr:
        elem = elem.strip().title()
        if elem != "":
            result.append(elem)
    return result

def get_csv_capitalized(var):
    """
    Converts a comma separated values in a string to an array of trimmed and capitalized strings
    :param var: the string with comma separated values to be converted
    :return: the array of trimmed and capitalized strings
    """
    names = var.split(',')
    return trim_capitalize(names)

def get_divisors(num):
    """
    Gets the divisors of a number.
    :param num: the number
    :return: the divisors
    """
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

def trim_min_max(arr, min_ = 0, max_ = sys.maxsize):
    """
    Trims the given array from the minimum value to the maximum one.
    :param arr: the array to be trimmed
    :param min_: the minimum value
    :param max_: the maximum value
    :return: the trimmed array
    """
    result = []
    for elem in arr:
        if min_ < elem < max_:
            result.append(elem)
    return result
