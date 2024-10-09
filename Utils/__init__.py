def take_input(msg):
    val = input(msg)
    return val

def take_float(msg):
    val = take_input(msg)
    try:
        return float(val)
    except ValueError as e:
        raise e

def take_temp():
    while True:
        try:
            val = take_float("Enter a temperature: ")
        except ValueError:
            print("Please enter a valid number")
            continue
        return val

def set_precision(val, precision = 2):
    return round(val, precision)