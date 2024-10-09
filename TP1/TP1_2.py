def get_even_numbers(num):
    if num < 0:
        raise ValueError("Number must be positive")
    if num > 100:
        raise ValueError("Number must be less than 100")
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
    return sum(list)

def product_list(list):
    result = list[0]
    for i in list[1:]:
        result *= i
    return result

def get_expression(list, sep):
    res = ''
    for i in range(len(list)):
        if i == len(list) - 1:
            res += str(list[i])
            break
        res += f'{list[i]} {sep} '
    return res