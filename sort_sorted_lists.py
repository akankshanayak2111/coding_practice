def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """

    ia = 0
    ib = 0

    res = []
    
    while ia < len(a) and ib < len(b):
        if a[ia] < b[ib]:
            out.append(a[ia])
            ia += 1
        else:
            out.append(b[ib])
            ib += 1

    out.extend(a[ia:])
    out.extend(b[ib:])

    return out
