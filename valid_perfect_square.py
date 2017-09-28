class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 1
        high = num/ 2
        mid = 0
        if num == 1:
            return True
        while low <= high:
            mid = (high-low)/2 + low
            
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            elif mid * mid > num:
                high = mid - 1
        return mid * mid == num
                
            