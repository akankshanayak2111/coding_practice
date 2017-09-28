class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while n > 1:
            if n % 2 != 0:
                return False
            n = n/2
        return n == 1        