import TP2.Models.TP2_2
import Utils
from Utils import *


def divide_ranges(arr: List[int], *ranges: tuple[int, int]) -> dict[tuple[int, int], List[int]]:
    result: dict[tuple[int, int], List[int]] = {}
    for range_ in ranges:
        num_range = []
        for num in arr:
            if range_[0] <= num <= range_[1]:
                num_range.append(num)
        result[range_] = num_range
    return result

def calc_freq(dic: dict[Any, int]) -> dict[Any, int]:
    freq: dict[Any, int] = {}
    total: int = 0
    for num in dic:
        total += dic[num]
    for num in dic:
        freq[num] = dic[num] / total
    return freq

def weighted_avg(arr: List[tuple[Any, List[int], int]]) -> float:
    vals: int = 0
    coef: int = 0
    for elem in arr:
        for val in elem[1]:
            vals += val * elem[2]
            coef += elem[2]
    return vals / coef


if __name__ == '__main__':
    mult_arr = Utils.gen_mult_array(precision = 1)
    arr = mult_arr[0]
    print(f'average: {TP2.Models.TP2_2.average_(*arr)}')
    ranged_arr = divide_ranges(arr, (0, 18), (19, 30), (31, 50), (51, 100))
    dict_len: dict[tuple[int, int], int] = {}
    for range_ in ranged_arr:
        dict_len[range_] = len(ranged_arr[range_])
    arr_freq = calc_freq(dict_len)
    ranged_freq_arr: List[tuple[Any, List[int], int]] = []
    for range_ in ranged_arr:
        ranged_freq: tuple[Any, List[int], int] = (range_, ranged_arr[range_], arr_freq[range_])
        ranged_freq_arr.append(ranged_freq)
    sum_freqs: float = 0
    for i in range(len(ranged_freq_arr)):
        sum_freqs += ranged_freq_arr[i][2]
        print(f'range: {ranged_freq_arr[i][0]} | freq: {ranged_freq_arr[i][2]} | vals: {ranged_freq_arr[i][1]}')
    print(f'sum_freqs: {sum_freqs}')
    print(f'weighted avg: {weighted_avg(ranged_freq_arr)}')
    Utils.graph_draw(ranged_arr)
