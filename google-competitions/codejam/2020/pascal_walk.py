def sol():
    n = int(input())
    if n <= 40:
        return [[i, 1] for i in range(1, n+1)]
    p = 0
    m = n - 40
    p2s = []
    while m > 0:
        if m%2:
            p2s.append(p+1)
        m //= 2
        p += 1
    left = True
    res = []
    for k in range(1, 41+len(p2s)):
        if k in p2s:
            u = [[k, i] for i in range(1, k+1)]
            res += u if left else u[::-1]
            left = not left
            
        else:
            res.append([k, 1] if left else [k, k])
    return res

t = int(input())
for i in range(1, t+1):
    res = sol()
    s = 'Case #{}:'.format(i)
    for p in res:
        s += '\n{} {}'.format(p[0], p[1])
    print(s)