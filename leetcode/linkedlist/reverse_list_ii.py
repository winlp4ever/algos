class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    root = ListNode(-1, head)
    r = root
    h = r.next
    i = 1
    while i < left:
      r = r.next
      h = r.next
      i += 1
    j = i
    curr = h
    while j < right:
      i_1 = curr.next
      curr.next = curr.next.next
      i_ = r.next
      r.next = i_1
      i_1.next = i_
      j += 1
    return root.next