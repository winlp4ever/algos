class Node(object):
  def __init__(self, key: int):
    self.data = key
    self.left = None 
    self.right = None


def inOrderSuccessor(root: Node, n: Node) -> Node:
  if n.right is not None:
    return findLeftMost(n.right)
  stk = None
  val = n.data
  curr = root
  while curr.data != val:
    if val > curr.data:
      curr = curr.right
    else:
      stk = curr
      curr = curr.left
  if not stk:
    return None
  if stk.right is not None:
    return findLeftMost(stk.right)
  return stk


def findNode(root: Node, val: int) -> Node:
  if root is None:
    return None
  if root.data == val:
    return root 
  if root.data < val:
    return findNode(root.right, val)
  return findNode(root.left, val)


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


def findLeftMost(n: Node) -> Node:
  current = n 
  if current is None:
    return None
  while current.left is not None:
    current = current.left
  return current


def test0():
  n = insert(None, 10)
  insert(n, 5)
  insert(n, 7)
  assert inOrderSuccessor(n, findNode(n, 7)).data == 10, "found %d, should be %d" % (inOrderSuccessor(n, findNode(n, 7)).data, 10)

def test1():
  n = insert(None, 10)
  insert(n, 5)
  insert(n, 7)
  insert(n, 9)
  insert(n, 8)
  assert inOrderSuccessor(n, findNode(n, 7)).data == 8, "found %d, should be %d" % (inOrderSuccessor(n, findNode(n, 7)).data, 8)

def test2():
  n = insert(None, 11)
  insert(n, 5)
  insert(n, 7)
  insert(n, 9)
  insert(n, 8)
  insert(n, 10)
  assert inOrderSuccessor(n, findNode(n, 7)).data == 8, "found %d, should be %d" % (inOrderSuccessor(n, findNode(n, 7)).data, 8)

def test3():
  n = insert(None, 10)
  insert(n, 5)
  insert(n, 7)
  insert(n, 9)
  insert(n, 8)
  insert(n, 11)
  assert inOrderSuccessor(n, findNode(n, 11)) == None, "found %d, should be %d" % (inOrderSuccessor(n, findNode(n, 11)).data, None)


if __name__ == '__main__':
  test0()
  test1()
  test2()
  test3()