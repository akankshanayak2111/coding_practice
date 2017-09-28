class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            d[s[i]] = i
            
        return max_len
            