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

memo[n][0] = 0

def foo(u, p):
    d = 0
    for cu, cp in zip(u, p):
        if cu > cp:
            return -1
        d += cu != cp
    return d

for i in range(n-1, -1, -1):
    for m, s in enumerate(digits):
        d = foo(bins[i], s)
        if d == -1:
            continue
        for j in range(k+1-d):
            recu = memo[i+1][j]
            if recu == -1:
                continue 
            memo[i][j+d] = 10 * d + m

if memo[0][k] >= 0:
    for i in range(n):
        print(memo[i][k] % 10, end='')
        k -= memo[i][k] // 10
    print()
                
else:
    print(-1)