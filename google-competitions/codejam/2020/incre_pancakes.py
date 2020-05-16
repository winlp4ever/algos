def sol():
    L, R = map(int, input().split())
    return rec(L, R, 1)

def rec(l, r, i):
    if i > max(l, r):
        return 0, l, r
    if l >= r:
        a, u, v = rec(l-i, r, i+1)
    else:
        a, u, v = rec(l, r-i, i+1)
    return 1+a, u, v


t = int(input())

for i in range(1, t+1):
    print('Case #{}: {} {} {}'.format(i, *sol()))