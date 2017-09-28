def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    

    for i in range(len(nums)):
        for i+1 in range(len(nums)):
            if nums[i] + nums[i+1] == 0:
                return True
    return False


def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""


    num_set = set(nums)
    for num in nums:
        if -num in num_set:
            return True
    return False
