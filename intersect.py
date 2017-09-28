class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return intersect(nums1, nums2)
    
def intersect(nums1, nums2):
    
    result = set()
    
    for num in nums1:
        if num in nums2:
            result.add(num)
            
    return list(result)