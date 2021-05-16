from typing import List
from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def rightSideView(root: TreeNode) -> List[int]:
  if root is None:
    return []
  q = deque([(1, root)])
  res = []
  while q:
    h, n = q.popleft()
    if n.right:
      q.append((h+1, n.right))
    if n.left:
      q.append((h+1, n.left))
    if h == len(res):
      continue
    res.append(n.val)
  return res