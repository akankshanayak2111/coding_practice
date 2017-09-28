def deduped(items):
    """Return new list from items with duplicates removed."""

    new_list = []

    seen = set()

    for item in items:
        if item not in seen:
            new_list.append(item)
            seen.add(item)

    return new_list