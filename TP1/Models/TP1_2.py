def get_even_numbers(num):
    """
    Gets all even numbers from 0 to the specified number.
    :param num: the number
    :return: the list of even numbers
    """
    if num < 0:
        raise ValueError("Number must be positive")
    if num > 25:
        raise ValueError("Number must be less than 25")
    result = []
    if num == 0:
        result.append(0)
        return result
    for i in range(num + 1):
        if i == 0:
            continue
        if i % 2 == 0:
            result.append(i)
    return result

def sum_list(list):
    """
    Sums all values in a list.
    :param list: the list
    :return: the sum of the values
    """
    return sum(list)

def product_list(list):
    """
    Calculates the product of all values in a list.
    :param list: the list
    :return: the product of the values
    """
    result = list[0]
    for i in list[1:]:
        result *= i
    return result

def get_expression(list, sep):
    """
    Concatenates a list of values adding a separator in-between.
    :param list: the list
    :param sep: the separator
    :return: the concatenated list
    """
    res = ''
    for i in range(len(list)):
        if i == len(list) - 1:
            res += str(list[i])
            break
        res += f'{list[i]} {sep} '
    return res