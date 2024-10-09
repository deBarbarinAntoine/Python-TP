import json
from random import random

# generate random int between min and max
def rand(min, max):
    return int(random() * (max - min) + min)

def get_greetings():
    json_greetings = json.JSONDecoder().decode(open('Assets/greetings.json').read())
    return json_greetings['greetings'], json_greetings['names']

_greetings, _names = get_greetings()

def assign_random_greeting(names = _names, greetings = _greetings):
    if len(names) == 0:
        names = _names
    result = []
    for name in names:
        result.append(greetings[rand(0, len(greetings) - 1)].format(name))
    return result

if __name__ == '__main__':
    greetings, names = get_greetings()
    print(assign_random_greeting(names, greetings))
