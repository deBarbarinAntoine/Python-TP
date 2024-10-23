import Utils
from Utils import *


def dice_throw(num: int = 1, val: int = 6) -> dict[int, int]:
    if num < 1 or val < 1:
        return {}
    result = []
    for i in range(num):
        result.append(random.randint(1, val))
    return Utils.list_to_dict(result)


if __name__ == '__main__':
    # print(Utils.sort_dict(dice_throw(10_000, 20), 'desc'))
    throws = Utils.gen_mult_array(nb = 10, len_range = (5, 50), val_range = (1, 1024))
    graph_draw(throws)