# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_balance(root):
            if not root:
                return 0
        
            ht_l = check_balance(root.left)
            ht_r = check_balance(root.right)
            if ht_l == -1 or ht_r == -1 or abs(ht_l - ht_r) > 1:
                return -1
            return 1 + max(ht_l, ht_r)
        return check_balance(root) != -1
        
        