class Node(object):
  def __init__(self, key: int):
    self.data = key
    self.left = None 
    self.right = None


def findNode(root: Node, val: int) -> Node:
  if root is None:
    return None
  curr = root
  while curr:
    if curr.data == val:
      return curr
    if curr.data < val:
      curr = curr.right
    else:
      curr = curr.left
  return None


def insert(node: Node, data: int) -> Node:
  if node is None:
    return Node(data)
  if data == node.data:
    return node
  if data > node.data:
    node.right = insert(node.right, data)
  else:
    node.left = insert(node.left, data)
  return node


def findMin(n: Node) -> Node:
  current = n 
  if current is None:
    return None
  while current.left is not None:
    current = current.left
  return current


def deleteNode(root: Node, key: int) -> Node:
  if root is None:
    return None
  if root.data < key:
    root.right = deleteNode(root.right, key)
    return root
  if root.data > key:
    root.left = deleteNode(root.left, key)
    return root
  u = findMin(root.right)
  if u is None:
    return root.left
  val = u.data
  r = deleteNode(root.right, val)
  root.data = val
  root.right = r
  return root

  