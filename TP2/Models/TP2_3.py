import statistics
import Utils


def variance(*num: float):
    return statistics.variance(num)


def variance_(*num: float):
    n: int = 0
    sum: int = 0
    sum_square: int = 0
    for i in num:
        n += 1
        sum += i
    avg = sum / n
    for i in num:
        sum_square += (i - avg) ** 2
    return sum_square / (n - 1)


def std_dev(*num: float):
    return statistics.stdev(num)

def std_dev_(*num: float):
    return variance_(*num) ** 0.5

def compare_funcs():
    arr = Utils.gen_array()
    print(f'statistics.variance: {variance(*arr)} | variance_: {variance_(*arr)}')
    print(f'statistics.std_dev: {std_dev(*arr)} | std_dev_: {std_dev_(*arr)}')

if __name__ == "__main__": compare_funcs()