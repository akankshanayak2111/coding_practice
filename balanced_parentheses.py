def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    parens = []

    for char in phrase:

        if char == "(":
            parens.append(char)
        elif char == ")":
            if not parens:
                return False
            else:
                parens.pop()

    return len(parens) == 0