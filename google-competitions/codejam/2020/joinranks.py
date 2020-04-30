t = int(input())

def sol(r, s):
    if r == 1:
        return []
    res = []
    for i in range(1, s):
        res.append([r * i, 1])
    res.append([s, r*s - s])
    rec = sol(r-1, s)
    for u, v in rec:
        if v == (r-1)*s - s:
            v += s
        res.append([u, v])
    return res
    
for i in range(1, t+1):
    r, s = map(int, input().split())
    solu = sol(r, s)
    print('Case #{}: {}'.format(i, len(solu)))
    for a, b in solu:
        print(a, b)