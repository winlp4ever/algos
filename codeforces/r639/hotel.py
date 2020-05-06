t = int(input())

def sol():
    n = int(input())
    a = list(map(int, input().split()))
    mrk = [False for _ in range(n)]
    for i in range(n):
        u = (i + a[i]) % n 
        if u < 0:
            u += n 
        if mrk[u]:
            return False 
        mrk[u] = True
    return True

for _ in range(t):
    print('YES' if sol() else 'NO')