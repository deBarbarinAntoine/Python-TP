import statistics
import Utils
from TP2.Models.TP2_2 import average_


def variance(*num: float):
    """
    This function calculates the variance of a list of numbers using the statistics module.
    :param num: the list of numbers
    :return: the variance
    """
    return statistics.variance(num)


def variance_(*num: float):
    """
    This function calculates the variance of a list of numbers using a custom algorithm.
    :param num: the list of numbers
    :return: the variance
    """
    
    sum_square: int = 0
    avg = average_(*num)
    
    for i in num:
        sum_square += (i - avg) ** 2
        
    return sum_square / (len(num) - 1)


def std_dev(*num: float):
    """
    Standard Deviation using the statistics module
    :param num: the list of numbers
    :return: the standard deviation
    """
    return statistics.stdev(num)

def std_dev_(*num: float):
    """
    Standard Deviation using the custom variance_ function
    :param num: the list of numbers
    :return: the standard deviation
    """
    return variance_(*num) ** 0.5

def compare_funcs():
    """
    This function shows the difference between the functions from the statistics module and my self-made ones.
    """
    arr = Utils.gen_array()
    print(f'statistics.variance: {variance(*arr)} | variance_: {variance_(*arr)}')
    print(f'statistics.std_dev: {std_dev(*arr)} | std_dev_: {std_dev_(*arr)}')

# comparing the statistics module functions with my self-made ones.
if __name__ == "__main__": compare_funcs()