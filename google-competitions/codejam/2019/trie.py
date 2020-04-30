import json
# easy implementation of trie in python
class Node:
    def __init__(self, c):
        self.c = c
        self.children = dict()
        self.end = False

    def toDict(self):
        return {
            'char': self.c,
            'end': self.end, 
            'children': {c: d.toDict() for c, d in self.children.items()}
        }

def addWord(root, w):
    h = len(w)
    ens = root.children
    h_ = 0 
    while h_ < h:
        c = w[h_]
        if c not in ens:
            newNode = Node(c)
            if h_ == h-1:
                newNode.end = True 
            ens[c] = newNode 
            ens = newNode.children
        else:
            node = ens[c]
            if h_ == h-1:
                node.end = True 
            ens = node.children
        h_ += 1

root = Node('')
words = ['world', 'wooh', 'word', 'wall', 'wo']
for w in words:
    addWord(root, w)
print(json.dumps(root.toDict(), indent=4))