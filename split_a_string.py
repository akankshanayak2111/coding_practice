def split(astring, splitter):
    """Split astring by splitter and return list of splits."""

    res = []
    i = 0

    while i <= len(astring):
        curr_idx = i

        i = astring.find(splitter, i)

        if i != -1:
            res.append(astring[curr_idx:i])
            i += len(splitter)
        else:
            res.append(astring[curr_idx:])
            break
    return res

