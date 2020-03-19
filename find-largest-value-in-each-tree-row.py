from collections import deque
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    '''
    breadth first search - O(n)
    '''
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        Q = deque([(root, 0)])
        height = 0
        res = []
        mx = -float('inf')
        while Q:
            v, h = Q.popleft()
            if h == height:
                if mx < v.val:
                    mx = v.val
            if h != height:
                res.append(mx)
                mx = v.val
                height = h
            if v.left:
                Q.append((v.left, h+1))
            if v.right:
                Q.append((v.right, h+1))
        res.append(mx)
        return res