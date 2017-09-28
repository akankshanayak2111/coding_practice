def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""


    count = {}

    for char in word:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    value_count = 0

    for value in count.values():
        if value % 2 != 0:
            value_count += 1
            
    if value_count > 1:
        return False
    else:
        return True