def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple."""

    

    if not nums:
        return (None, None)

    max_num = nums[0]
    min_num = nums[0]

    for num in nums:
        if num > max_num:
            max_num = num

        if num <= min_num:
            min_num = num

    return (min_num, max_num)

