import TP2.Models.TP2_2
from Utils import *


def divide_ranges(arr: List[int], *ranges: tuple[int, int]) -> dict[tuple[int, int], List[int]]:
    """
    Divides an array of values according to the ranges.
    :param arr: the array of values
    :param ranges: the ranges of values to divide the array into
    :return: the dictionary of ranges and sub-lists
    """
    
    # create the dictionary holding the results
    result: dict[tuple[int, int], List[int]] = {}
    
    # range through the ranges
    for range_ in ranges:
        num_range = []
        
        # add the value to the sub-list if it's in range
        for num in arr:
            if range_[0] <= num <= range_[1]:
                num_range.append(num)
        
        # add the sub-list to the result dictionary
        result[range_] = num_range
        
    return result

def calc_freq(dic: dict[Any, int]) -> dict[Any, int]:
    """
    Calculates the frequency of each value in dic.
    :param dic: the dictionary of values
    :return: a dictionary holding the frequency of each value in dic
    """
    freq: dict[Any, int] = {}
    total: int = 0
    
    # calculate the total number of values
    for num in dic:
        total += dic[num]
        
    # calculate the frequency of each entry in the dictionary
    for num in dic:
        freq[num] = dic[num] / total
        
    return freq

def weighted_avg(arr: List[tuple[Any, List[int], int]]) -> float:
    """
    Calculates the weighted average of an array of values.
    :param arr: the array of values
    :return: the weighted average
    """
    vals: int = 0
    coef: int = 0
    
    # calculate the values and the coefficients
    for elem in arr:
        for val in elem[1]:
            vals += val * elem[2]
            coef += elem[2]
            
    # return the weighted average
    return vals / coef


# testing the functions in the terminal
if __name__ == '__main__':
    
    # creating an array
    arr = gen_array(precision = 1)
    
    # print the average of the array
    print(f'average: {TP2.Models.TP2_2.average_(*arr)}')
    
    # divide the array by ranges
    ranged_arr = divide_ranges(arr, (0, 18), (19, 30), (31, 50), (51, 100))
    
    # create a dictionary with the ranges and the number of values in each one
    dict_len: dict[tuple[int, int], int] = {}
    for range_ in ranged_arr:
        dict_len[range_] = len(ranged_arr[range_])
        
    # calculate the frequency of each range provided
    arr_freq = calc_freq(dict_len)
    
    ranged_freq_arr: List[tuple[Any, List[int], int]] = []
    
    # add the frequency of each range to a comprehensive list
    for range_ in ranged_arr:
        ranged_freq: tuple[Any, List[int], int] = (range_, ranged_arr[range_], arr_freq[range_])
        ranged_freq_arr.append(ranged_freq)
        
    # print the results of the analysis
    sum_freqs: float = 0
    for i in range(len(ranged_freq_arr)):
        sum_freqs += ranged_freq_arr[i][2]
        print(f'range: {ranged_freq_arr[i][0]} | freq: {ranged_freq_arr[i][2]} | vals: {ranged_freq_arr[i][1]}')
    print(f'sum_freqs: {sum_freqs}')
    
    # calculate and print the weighted average
    print(f'weighted avg: {weighted_avg(ranged_freq_arr)}')
    
    # draw the graph in the file `Data/graph.png`
    graph_draw(ranged_arr)
