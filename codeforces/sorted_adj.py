def sol():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    i = 0
    res = []
    pos = (n-1)//2
    while len(res) < n:
        if i % 2 == 0:
            pos = pos-i
        else: 
            pos = pos+i 
        res.append(str(a[pos]))
        i += 1
    return res 

t = int(input())
for i in range(t):
    print(' '.join(sol()))