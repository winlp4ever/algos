import sys

cmp = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
S = 'ABCDE'

def phase(vs, sol, pos):
    cs = {i: [] for i in range(5) if i not in sol}
    for k in vs:
        idx = 5*k + pos
        print(idx)
        sys.stdout.flush()
        c = input()
        cs[cmp[c]].append(k)
    u = min([i for i in cs], key=lambda v: len(cs[v]))
    sol.append(u)
    for i in cs:
        if i == u:
            continue
        for idx in cs[i]:
            vs.remove(idx)

def sol():
    vals = {i for i in range(119)}
    sol = []
    for pos in range(1, 6):
        phase(vals, sol, pos)
    print(''.join(map(lambda u: S[u], sol)))
    sys.stdout.flush()
    _ = input()

t, w = map(int, input().split())
for _ in range(t):
    sol()
    