import json
from random import random


def rand(min_, max_):
    """
    Generates a random int between min_ and max_ including min_ but excluding max_
    :param min_: the minimum value
    :param max_: the maximum value
    :return: the random int between min_ and max_
    """
    return int(random() * (max_ - min_) + min_)

def get_greetings(from_ = 'Data/greetings.json'):
    """
    Gets the list of greetings and names from the JSON file
    :param from_: the path of the JSON file
    :return: a Tuple with the list of greetings and the list of names
    """
    json_greetings = json.JSONDecoder().decode(open(from_).read())
    return json_greetings['greetings'], json_greetings['names']

def assign_random_greeting(names = [], greetings = []):
    """
    Assigns a random greeting to a name
    :param names: the list of names
    :param greetings: the list of greetings
    :return: the list of greetings randomly assigned to the names
    """
    
    # checking if the values are empty
    if len(names) == 0 or len(greetings) == 0:
        
        # retrieve the default values from the JSON file
        _greetings, _names = get_greetings()
        
        if len(names) == 0:
            names = _names
        if len(greetings) == 0:
            greetings = _greetings
            
    result = []
    for name in names:
        result.append(greetings[rand(0, len(greetings) - 1)].format(name))
    return result

# To test the TP1_3 
if __name__ == '__main__':
    greetings, names = get_greetings('../Data/greetings.json')
    print(assign_random_greeting(names, greetings))
