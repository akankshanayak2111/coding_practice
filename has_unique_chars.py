def has_unique_chars(word):
    """Does word contains unique set of characters?"""


    count = {}

    for letter in word:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1

    for value in count.values():
        if value > 1:
            return False
    return True