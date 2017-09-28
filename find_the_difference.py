class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = make_dict(s)
        b = make_dict(t)
        
        return diff(a, b)
    
    
def make_dict(string):
    count = {}
    
    for letter in string:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
    return count

def diff(a, b):
    
    for k, v in b.items():
        if k not in a:
            return k
        elif k in a and b[k] != a[k]:
            return k