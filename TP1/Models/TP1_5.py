
def is_leap_year(year):
    """
    Checks if a year is a leap year
    :param year: the year
    :return: True if the year is a leap year, False otherwise. Returns False if year is not an int.
    """
    try:
        year = int(year)
    except ValueError:
        return False
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
