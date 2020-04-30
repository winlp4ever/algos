n, u = map(int, input().split())
k = n-u

graph = {i: [] for i in range(1, n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

class Node:
    def __init__(self, i):
        self.i = i
        self.children = []

root = Node(1)
Q = [root]
marked = [False for i in range(1, n+1)]
marked[0] = True

while Q:
    node = Q.pop()
    for j in graph[node.i]:
        if marked[j-1]:
            continue
        nj = Node(j)
        node.children.append(nj)
        Q.append(nj)
        marked[j-1] = True

memo = [0 for _ in range(1, n+1)]
def rec(node, memo):
    sm = 1 if node.i != 1 else 0
    for v in node.children:
        sm += rec(v, memo)
    memo[node.i-1] = sm
    return sm

rec(root, memo)
print(memo)
memo.sort(reverse=True)

print(sum(memo[:k]))



