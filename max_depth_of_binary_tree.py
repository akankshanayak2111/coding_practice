# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return depth(root)

def depth(root):
    
    if not root:
        return 0
    
    return 1 + max(depth(root.left), depth(root.right))