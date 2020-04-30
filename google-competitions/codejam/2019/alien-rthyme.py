def addWord(root, w):
    h = len(w)
    ens = root['children']
    h_ = 0 
    while h_ < h:
        c = w[h_]
        if c not in ens:
            newNode = {'c': c, 'end': False, 'children': dict()}
            if h_ == h-1:
                newNode['end'] = True 
            ens[c] = newNode 
            ens = newNode['children']
        else:
            node = ens[c]
            if h_ == h-1:
                node['end'] = True 
            ens = node['children']
        h_ += 1



def rec(node, nbPairs):
    sm = 0
    if node['end']:
        sm += 1
    for _, n in node['children'].items():
        sm += rec(n, nbPairs)
    if sm >= 2 and node['c'] != '':
        nbPairs[0] += 1
        return sm - 2
    return sm

t = int(input())
for i in range(1, t+1):
    root = {
        'c': '',
        'end': False,
        'children': dict()
    }
    nbPairs = [0]
    n = int(input())
    words = []
    for _ in range(n):
        w = input().strip()
        addWord(root, w[::-1])
        words.append(w[::-1])
    
    rec(root, nbPairs)
    print('Case #%d: %d' % (i, nbPairs[0]*2))
    
    
    
