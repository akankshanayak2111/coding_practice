def is_leap_year(year):
    """Is this year a leap year?

    Every 4 years is a leap year::

        >>> is_leap_year(1904)
        True

    Except every hundred years::

        >>> is_leap_year(1900)
        False

    Except-except every 400::

        >>> is_leap_year(2000)
        True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True



def days_in_month(date):
    """How many days are there in a month?"""

    date_list = date.split(" ")

    thirty_day_months = set([4, 6, 9, 11])

    thirty_one_day_months = set([1, 3, 5, 7, 8, 10, 12])

    if int(date_list[0]) == 2:
        if is_leap_year(int(date_list[1])):
            return 29
        else:
            return 28

    if int(date_list[0]) in thirty_day_months:
        return 30
    elif int(date_list[0]) in thirty_one_day_months:
        return 31
