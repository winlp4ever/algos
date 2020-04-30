t = int(input())

def sol():
    x, y = map(int, input().split())
    if x >= 0:
        dx = 'E'
        dx_ = 'W'
    else:
        dx = 'W'
        dx_ = 'E'
        x = -x
    if y >= 0:
        dy = 'N'
        dy_ = 'S'
    else:
        dy = 'S'
        dy_ = 'N'
        y = -y

    sm = x + y
    if not sm % 2:
        return 'IMPOSSIBLE'
    sm_ = sm 
    U = 0
    i = 0
    while sm_:
        sm_ //= 2
        U += 2 ** i
        i += 1
    diff = (U-sm) // 2
    #print(U, sm, i)
    negs = set()
    diff_ = diff 
    j = 0
    while diff_:
        if diff_ % 2:
            negs.add(j)
        diff_ //= 2
        j += 1
    x_ = x 
    Qx = set()
    k = 0
    while x_:
        if x_ % 2:
            Qx.add(k)
            if k in negs:
                x_ += 1
        x_ //= 2
        k += 1
    
    res = ''
    for h in range(i):
        if h in Qx:
            if h in negs:
                res += dx_
            else:
                res += dx
        else:
            if h in negs:
                res += dy_ 
            else:
                res += dy
    return res

for i in range(1, t+1):
    print('Case #{}: {}'.format(i, sol()))