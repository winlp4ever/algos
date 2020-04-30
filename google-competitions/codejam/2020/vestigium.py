t = int(input())

def case():
    n = int(input())
    cs = [set() for _ in range(n)]
    k = 0
    r = 0
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(n):
            cs[j].add(arr[j])
        k += arr[i]
        if len(set(arr)) < n:
            r += 1
    c = sum([len(cs[j]) < n for j in range(n)])
    return k, r, c

for i in range(1, t+1):
    k, r, c = case()
    print('Case #{}: {} {} {}'.format(i, k, r, c))
        
        