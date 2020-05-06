t = int(input())
def sol():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    a = dict()
    un = []
    i = 0
    for u in nums:
        if u not in a:
            a[u] = i
            un.append(str(u))
            i += 1
    if len(a) > k:
        return -1
    un += ['1'] * (k-i)
    return str(k*n) + '\n' + ' '.join(un * n)

for _ in range(t):
    print(sol())