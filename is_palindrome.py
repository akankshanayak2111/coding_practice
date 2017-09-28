def is_palindrome(word):
    """Return True/False if this word is a palindrome."""

    for i in range(len(word)/2):
        if word[i] != word[-i-1]:
            return False

    return True