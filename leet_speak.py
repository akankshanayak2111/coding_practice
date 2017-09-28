def translate_leet(phrase):
    """Translates input into "leet-speak"."""

    translate = {
    'a': '@',
    'o': '0',
    'e': '3',
    'l': '1',
    's': '5',
    't': '7',
    }

    leet = []

    for char in phrase:
        if char.lower() in translate:
            leet.append(translate[char])
        else:
            leet.append(char)

    return ''.join(leet)
