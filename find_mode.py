def find_mode(nums):
    """Find the most frequent num(s) in nums."""

    count = {}
    mode = set()
    max_v = 0

    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    for k, v in count.items():
        if v > max_v:
            max_v = v
            mode.add(k)

    return mode
