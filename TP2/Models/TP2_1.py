import Utils


def is_perfect(num: int) -> bool:
    """
    Checks if the given number is a perfect number.
    :param num: the number to be checked
    :return: True if the number is perfect, False otherwise
    """

    # get the divisors
    divisors = Utils.trim_min_max(Utils.get_divisors(num), 0, num)

    return sum(divisors) == num

if __name__ == '__main__':
    print(is_perfect(8128))