t = int(input())

def bprint(arr):
    s = 'POSSIBLE'
    n = len(arr)
    for i in range(n):
        s += '\n'
        for j in range(n):
            s += str(arr[i][j])
            if j < n-1:
                s += ' '
    return s

def sol():
    n, k = map(int, input().split())
    print('**k = %d' % k)
    k_ = k
    arr = []
    if k % n == 0:
        u = k // n
        r1 = [u] + [i for i in range(1, n+1) if i != u]
        for i in range(n):
            arr.append(r1[n-i:] + r1[:n-i])
        return bprint(arr)

    if n == 2 or n == 3:
        return 'IMPOSSIBLE'

    reverse = k > (n**2 + n) // 2
    if reverse:
        k = n**2 + n - k

    l = k % n
    u = k // n
    if u == 1 and l == 1:
        return 'IMPOSSIBLE'
    if l >= 3:
        v = u + 1
        w = u + 2
        comp = [i for i in range(1, n+1) if i not in {w, u, v}]
        r1 = [v, u] + comp
        r1 = r1[:l-1] + [w] + r1[l-1:]
        # k = u * n + l = (l-2)*(u+1) + (u+2) + (n-l+2)*u = (l-2)*v + w + (n-l+2)*u
        for i in range(n):
            if i < l-2:
                arr.append(r1[n-i:] + r1[:n-i])
            elif i < l-1:
                arr.append(r1[1:] + r1[:1])
            else:
                arr.append(r1[n-i+1:] + r1[:n-i+1])
        
    elif u >= 2:
        v = u - 1
        w = u + l + 1
        comp = [i for i in range(1, n+1) if i not in {w, u, v}]
        r1 = [u, w] + comp + [v]
        for i in range(n):
            arr.append(r1[n-i:] + r1[:n-i])
        arr[-2], arr[-1] = arr[-1], arr[-2]
    else:
        rs = [set() for i in range(n)]
        cs = [set() for i in range(n)]
        for i in range(n):
            if i < n-2:
                rs[i].add(1)
                cs[i].add(1)
            else:
                rs[i].add(2)
                cs[i].add(2)
        arr = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    arr[i][j] = 1 if i < n-2 else 2
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for h in range(1, n+1):
                    if i != j and (h not in rs[i]) and (h not in cs[j]):
                        arr[i][j] = h
                        cs[j].add(h)
                        rs[i].add(h)
                        break 

    if reverse:
        for i in range(n):
            for j in range(n):
                arr[i][j] = n+1 - arr[i][j]
    check(arr, k_)
    return bprint(arr)

def check(arr, k):
    n = len(arr)
    trace = 0
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    for i in range(n):
        trace += arr[i][i]
        for j in range(n):
            rows[i].add(arr[i][j])
            cols[j].add(arr[i][j])
    
    if trace != k:
        print('err - trace not true k={}'.format(k))
    for i in range(n):
        if len(rows[i]) < n or len(cols[i]) < n:
            print('err - eles not distinct')
    
    
for i in range(1, t+1):
    print('Case #{}: {}'.format(i, sol()))
        