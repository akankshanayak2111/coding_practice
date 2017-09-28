def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    higher_than = 0
    lower_than = 101

    num_guesses = 0
    guess = None
    

    while guess != val:
        guess = (lower_than - higher_than)/ 2 + higher_than
        num_guesses += 1
        
        if val < guess:
            lower_than = guess
        elif val > guess:
            higher_than = guess

    return num_guesses