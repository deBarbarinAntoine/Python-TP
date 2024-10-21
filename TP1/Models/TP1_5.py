def is_leap_year(year):
    try:
        year = int(year)
    except ValueError:
        return False
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)