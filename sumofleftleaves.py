# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isLeaf(node):
    return not node.left and not node.right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root or isLeaf(root):
            return 0
        a = self.sumOfLeftLeaves(root.right)
        if not root.left:
            return a
        if isLeaf(root.left):
            return root.left.val + a
        return self.sumOfLeftLeaves(root.left) + a