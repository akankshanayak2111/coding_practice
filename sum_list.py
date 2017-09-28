def sum_list(nums):
    """Using recursion, return the sum of numbers in a list."""

    if not nums:
        return 0

    return nums[0] + sum_list(nums[1:])