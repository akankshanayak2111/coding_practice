def print_recursively(lst):
    """Print items in the list, using recursion."""

    if not lst:
        return

    else:
        print lst[0]
        print_recursively(lst[1:])