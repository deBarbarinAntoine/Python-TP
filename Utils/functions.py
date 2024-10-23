import csv
import itertools
import json
import random
import sys
from typing import *
import matplotlib.pyplot as plt


def set_precision(val, precision=2):
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
    divisors = []

    for i in range(1, int(num ** 0.5) + 1):

        if num % i == 0:
            divisors.append(i)

            if i != num // i:
                divisors.append(num // i)

    return divisors


def trim_min_max(arr, min_=0, max_=sys.maxsize):
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


def list_to_dict(arr: List[Any]) -> dict[Any, int]:
    result: dict[Any, int] = {}
    for elem in arr:
        if elem not in result:
            result[elem] = 1
        else:
            result[elem] += 1
    return result


def sort_dict(dic: dict[Any, int], order: str = 'asc') -> dict[Any, int]:
    match order:
        case 'asc':
            return dict(sorted(dic.items(), key=lambda item: item[1]))
        case 'desc':
            return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        case _:
            return {}


def gen_array(len_range: tuple[int, int] = (5, 100), val_range: tuple[int, int] = (0, 100), precision: int = 0) -> List[int | float]:
    """
    Generates a random array with given range and precision.
    :param len_range: the range of length in the format tuple(min, max) - Default = (5, 100)
    :param val_range: the range of values in the format tuple(min, max) - Default = (0, 100)
    :param precision: the number of digits to round to - Default = 0
    :return: the generated array
    """

    # setting the min and max range of the array to generate
    range_min, range_max = val_range

    # return empty List if range is null
    if range_min == range_max:
        return []

    # make sure range_min < range_max
    if range_min > range_max:
        range_max, range_min = range_min, range_max

    # setting the min and max length of the array to generate
    len_min, len_max = len_range

    # return empty List if any of the lengths are null or negative
    if len_min < 0 or len_max < 0:
        return []

    # make sure len_min < len_max
    if len_min > len_max:
        len_min, len_max = len_max, len_min

    # create empty array
    array_: List[float] = []

    # generate the length of the array
    if len_min == len_max:
        len_ = len_min
    else:
        len_ = random.randint(len_min, len_max)

    # generate every value of the array
    for _ in range(len_):
        array_.append(set_precision(random.random() * (range_max - range_min) + range_min, precision))

    return array_


def gen_mult_array(nb: int = 10, len_range: tuple[int, int] = (5, 100), val_range: tuple[int, int] = (0, 100), precision: int = 0) -> List[List[int | float]]:
    """
    Generates multiple arrays with given range and precision.
    :param nb: the number of arrays to be generated
    :param len_range: the range of length in the format tuple(min, max) - Default = (5, 100)
    :param val_range: the range of values in the format tuple(min, max) - Default = (0, 100)
    :param precision: the number of digits to round to - Default = 0
    :return: the List of generated arrays
    """
    array_: List[List[int | float]] = []
    for _ in range(nb):
        array_.append(gen_array(len_range, val_range, precision))
    return array_


def graph_draw(data: list | dict | tuple | set):
    fig, ax = plt.subplots()
    ax.boxplot(data, showmeans = True)
    plt.xlabel("groups")
    if type(data) == dict:
        ax.set_xticklabels(data.keys())
    plt.ylabel("values")
    plt.savefig('../Data/graph.png')


def get_list_from_json(filename: str) -> list:
    try:
        json_file = open(filename, 'r')
        arr = json.JSONDecoder().decode(json_file.read())
        json_file.close()
        return arr
    except json.decoder.JSONDecodeError:
        raise FileNotFoundError


def get_list_from_csv(filename: str) -> list:

    try:
        file = open(filename, 'r')
    except FileNotFoundError as e:
        raise e

    raw_content = list(csv.reader(file, delimiter = ','))

    iterable_content = itertools.chain.from_iterable(raw_content)

    file.close()

    return list(iterable_content)

