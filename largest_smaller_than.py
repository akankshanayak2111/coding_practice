def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""

    max_num = nums[0]
    max_idx = 0

    for idx, num in enumerate(nums):
        if num > max_num and num < xnumber:
            max_num = num
            max_idx = idx

    return max_idx