def replace_vowels(chars):
    """Given list of chars, return a new copy, but with vowels replaced by '*'."""

    vowels = set(['a','e','i','o','u'])

    new_list = []

    for char in chars:
        if char in vowels:
            char = '*'
        new_list.append(char)

    return new_list