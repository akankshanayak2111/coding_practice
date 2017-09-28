def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    count = {}

    for char in sentence:
        if char.isalpha():
            if char.lower() not in count:
                count[char] = 1
            else:
                count[char.lower()] += 1

    if len(count.keys) != 26:
        return False
    else:
        return True
