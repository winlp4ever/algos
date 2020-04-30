n, k = map(int, input().split())
 
bins = [input() for _ in range(n)]

 
digits = [
    '1110111',
    "0010010", 
    "1011101", 
    "1011011", 
    "0111010", 
    "1101011", 
    "1101111", 
    "1010010", 
    "1111111", 
    "1111011"
]
 
memo = [[-1 for _ in range(k+1)] for _ in range(n+1)]
filled = [[False for _ in range(k+1)] for _ in range(n+1)]
 
memo[n][0] = 0
for j in range(k+1):
    filled[n][j] = True
 
def foo(u, p):
    d = 0
    for i in range(7):
        if u[i] == '1' and p[i] == '0':
            return -1
        if u[i] == '0' and p[i] == '1':
            d += 1
    return d

def rec(i, j, memo):
    if filled[i][j]:
        return memo[i][j]
    res = -1
    for m, s in enumerate(digits):
        d = foo(bins[i], s)
        if d == -1 or j < d:
            continue
        recu = rec(i+1, j-d, memo)
        if recu == -1:
            continue 
        res = 10 * d + m
 
    memo[i][j] = res
    filled[i][j] = True
    return res
 
 
rec(0, k, memo)
if memo[0][k] >= 0:
    for i in range(n):
        print(memo[i][k] % 10, end='')
        k -= memo[i][k] // 10
    print()
else:
    print(-1)