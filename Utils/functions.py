import csv
import itertools
import json
import random
import sys
from typing import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import ttk


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

def get_csv_numbers(var, type_: str = 'float'):
    """
    Converts a comma separated values in a string to an array of trimmed numbers.
    :param var: the string with comma separated values to be converted
    :param type_: the type of number to be converted into
    :return: the array of trimmed numbers
    :raise ValueError: if any element of var is not a number of the specified type
    """
    values = var.split(',')
    
    for i in range(len(values)):
        if type_ == 'float':
            try:
                values[i] = float(values[i].strip())
            except ValueError:
                raise ValueError('Incorrect decimal number format.')
        elif type_ == 'int':
            try:
                values[i] = int(values[i].strip())
            except ValueError:
                raise ValueError('Incorrect integer number format.')
    
    return values


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
    """
    Converts a list to a dictionary of {value: occurrences}.
    :param arr: the list to be converted
    :return: the converted list
    """
    result: dict[Any, int] = {}
    for elem in arr:
        if elem not in result:
            result[elem] = 1
        else:
            result[elem] += 1
    return result


def sort_dict(dic: dict[Any, int], order: str = 'asc') -> dict[Any, int]:
    """
    Sorts the given dictionary according to the given order.
    :param dic: the dictionary to be sorted
    :param order: the order to be sorted with
    :return: the sorted dictionary
    """
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
        if precision == 0:
            array_.append((int(random.random() * 1_000_000_000_000) % int(range_max - range_min + 1)) + range_min)
        else:
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


def graph_draw(data: list | dict | tuple | set, frame: ttk.Frame = None) -> None:
    """
    Draws a graph with given data and, if there is a frame,
     draw it there, else, save it in `Data/graph.png`.
    :param data: the data to be drawn
    :param frame: the frame to be drawn
    """
    fig, ax = plt.subplots()
    ax.boxplot(data, showmeans = True)
    plt.xlabel("groups")
    if type(data) == dict:
        ax.set_xticklabels(data.keys())
    plt.ylabel("values")
    if frame:
        for child in frame.winfo_children():
            child.destroy()
        canvas = FigureCanvasTkAgg(fig,
                                   master = frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()
        canvas.get_tk_widget().pack()
    else:
        plt.savefig('../Data/graph.png')
        
def bar_graph_draw(data: dict, frame: ttk.Frame = None) -> None:
    """
    Draws a bar graph with the given data dictionary and, if there is a frame,
     draw it there, else, save it in `Data/bar_graph.png`.
    :param data: the data dictionary
    :param frame: the ttk.Frame to draw the bar graph
    """
    values = list(data.keys())
    occurrences = list(data.values())
    
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(values, occurrences, color ='blue',
            width = 0.4)
    
    plt.xlabel("Values")
    plt.ylabel("No. of occurrences")
    
    if frame:
        for child in frame.winfo_children():
            child.destroy()
        canvas = FigureCanvasTkAgg(fig,
                                   master = frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas,
                                       frame)
        toolbar.update()
        canvas.get_tk_widget().pack()
    else:
        plt.savefig('../Data/bar_graph.png')


def get_list_from_json(filename: str) -> list:
    """
    Gets a list from a JSON file.
    :param filename: the path of the JSON file
    :return: the list
    """
    try:
        json_file = open(filename, 'r')
        arr = json.JSONDecoder().decode(json_file.read())
        json_file.close()
        return arr
    except json.decoder.JSONDecodeError:
        raise FileNotFoundError


def get_list_from_csv(filename: str) -> list:
    """
    Gets a list from a CSV file.
    :param filename: the path of the CSV file
    :return: the list
    """

    try:
        file = open(filename, 'r')
    except FileNotFoundError as e:
        raise e

    raw_content = list(csv.reader(file, delimiter = ','))

    iterable_content = itertools.chain.from_iterable(raw_content)

    file.close()

    return list(iterable_content)

