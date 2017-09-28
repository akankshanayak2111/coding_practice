def find_longest_word(words):
    """Return longest word in list of words."""

    max_l = 0

    for word in words:
        if len(word) > max_l:
            max_l = len(word)

    return max_l