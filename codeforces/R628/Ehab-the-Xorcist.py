def sol():
    u, v = map(int, input().split())
    if u > v or (u-v) % 2 != 0:
        return -1
    if u == v:
        if u == 0:
            return 0
        else:
            return '1\n%d' % u
    x = (v-u) // 2

    a, b = 0, 0
    i = 1
    u_ = u 
    x_ = x
    while u_ or x_:
        m, n = u_%2, x_%2
        if n == 1:
            if m == 1:
                return '3\n{} {} {}'.format(u, x, x)
            else:
                a += i 
                b += i 
        else:                
            if m == 1:
                a += i 
        u_ //= 2
        x_ //= 2
        i *= 2
    return '2\n%d %d' % (a, b)
print(sol())
