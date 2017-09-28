def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    while num:
        digit = num % 10
        print digit
        num = (num - digit)/10

        