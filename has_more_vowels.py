def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?"""

    vowels = set(['a', 'e', 'i', 'o', 'u'])

    count_v = 0

    for letter in word:
        if letter.lower() in vowels:
            count_v += 1

    if count_v > (len(word) - count_v):
        return True
    else:
        return False