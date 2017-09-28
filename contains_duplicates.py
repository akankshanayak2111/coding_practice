class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return duplicates(nums)
    
def duplicates(nums):
    
    count = {}
    
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            return True
    return False