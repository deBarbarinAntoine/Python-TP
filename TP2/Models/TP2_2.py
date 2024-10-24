import statistics
from Utils import *


def average(*nums: float) -> float:
    """
    Calculates the average of a list of numbers using the statistics module
    :param nums: the values
    :return: the results
    """
    return statistics.mean(nums)


def average_(*nums: float) -> float:
    """
    Calculates the average of a list of numbers using a self-made algorithm
    :param nums: the values
    :return: the results
    """
    return sum(nums) / len(nums)


def median(*nums: float) -> float:
    """
    Calculates the median of a list of numbers using the statistics module
    :param nums: the values
    :return: the results
    """
    return statistics.median(nums)


def median_(*nums: float) -> float:
    """
    Calculates the median of a list of numbers using a self-made algorithm
    :param nums: the values
    :return: the results
    """
    nums = sorted(nums)
    if len(nums) % 2 == 0:
        middle = len(nums) // 2
        return average_(nums[middle], nums[middle - 1])
    return nums[int(len(nums) / 2)]


def compare_funcs():
    """Compare the functions using the statistics module and the self-made algorithms"""
    array_ = gen_array()
    print(f'statistics.average: {average(*array_)} | average_: {average_(*array_)}')
    print(f'statistics.median: {median(*array_)} | median_: {median_(*array_)}')

# To compare the library functions and my self-made ones
if __name__ == '__main__': compare_funcs()
