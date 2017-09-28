def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""


    lucky_nums = []
    nums = range(1, 11)

    for num in range(n):
        num = random.choice(nums)
        nums.remove(num)
        lucky_nums.append(num)

    return lucky_nums