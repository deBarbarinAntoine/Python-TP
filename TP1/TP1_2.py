def get_even_numbers(num):
    result = []
    for i in range(num):
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