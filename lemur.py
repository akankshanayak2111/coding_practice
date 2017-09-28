def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    jump = 0
    at = 0

    while at < len(branches)-1:
        at +=2
        if at >= len(branches) or branches[at] == 1:
            at -= 1
        jump += 1

    return jump

