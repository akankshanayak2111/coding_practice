class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res, stack = [], []
        cache = {}
        
        for num in nums:
            while stack and stack[-1] < num:
                cache[stack.pop()] = num
            stack.append(num)
                
        res = [-1] * len(findNums)
        
        for i, num in enumerate(findNums):
            if num in cache:
                res[i] = cache[num]
        return res
                