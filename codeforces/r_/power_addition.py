def sol():
    n = int(input())
    a = list(map(int, input().split()))
    mxs = [a[0]]
    M = 0
    for u in a[1:]:
        mx = max(u, mxs[-1])
        if M < mx - u:
            M = mx - u
        mxs.append(mx)
    res = 0
    while M:
        M //= 2
        res += 1
    return res 

t = int(input())
for _ in range(t):
    print(sol())
