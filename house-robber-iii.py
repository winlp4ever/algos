'''
search for problem on leetcode
the nature is: given a binary tree with weighted vertices. find out the set of vertices with maximum weight sum where 
no 2 vertices are adjacent.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x 
        self.left = None 
        self.right = None

class Solution:
    '''
    complexity: O(n)
    idea: recurrent or dynamic programming;
    you can do this either with dynamic programming or with a smart recurrent function, 
    the function takes as input a tree node and return, not only the maximum subset weight (following defined constraint)
    of the subtree with the current node as the root, but also the maximum subset weight of the subtree with node.right and 
    node.left
    '''
    def rob(self, root: TreeNode):
        '''
        complexity: O(n)
        idea: recurrent or dynamic programming;
        you can do this either with dynamic programming or with a smart recurrent function, 
        the function takes as input a tree node and return, not only the maximum subset weight (following defined constraint)
        of the subtree with the current node as the root, but also the maximum subset weight of the subtree with node.right and 
        node.left as root respectively
        '''
        def rec(node):
            if not node:
                return 0, 0, 0
            a = node.val
            u, v, w = rec(node.left)
            x, y, z = rec(node.right)
            return max(a+v+w+y+z, u+x), u, x
        res, _, _ = rec(root)
        return res
            