def is_prime(num):
    """Is a number a prime number?"""
    if num < 2:
        return False

    # if num == 2:
        return True


    for n in range(2, num):
        if num % n == 0:
            return False

    return True