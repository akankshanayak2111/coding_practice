def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    
    def rec_index(needle, haystack, start_at):

        if start_at == len(haystack):
            return None

        if haystack[start_at] == needle:
            return start_at

        return rec_index(needle, haystack, start_at+1)


    return rec_index(needle, haystack, 0)