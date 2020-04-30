def sol():
    p, q = map(int, input().split())
    xs = dict()
    ys = dict()

    for _ in range(p):
        x, y, d = input().split()
        x, y = int(x), int(y)
        if d == 'N':
            if y+1 not in ys:
                ys[y+1] = [0, 0]
            ys[y+1][1] += 1
        if d == 'S':
            if y not in ys:
                ys[y] = [0, 0]
            ys[y][0] += 1
        if d == 'W':
            if x not in xs:
                xs[x] = [0, 0]
            xs[x][0] += 1
        if d == 'E':
            if x+1 not in xs:
                xs[x+1] = [0, 0]
            xs[x+1][1] += 1
    xs_ = sorted([x for x in xs])
    ys_ = sorted([y for y in ys])
    cx = sum([xs[u][0] for u in xs_])
    cy = sum([ys[v][0] for v in ys_])
    mx, my = cx, cy 
    ix, iy = 0, 0
    for i in range(len(xs_)):
        if xs_[i] == 0:
            continue
        cx += xs[xs_[i]][1] - xs[xs_[i]][0]
        if cx > mx:
            mx = cx 
            ix = xs_[i]
    for i in range(len(ys_)):
        if ys_[i] == 0:
            continue 
        cy += ys[ys_[i]][1] - ys[ys_[i]][0]
        if cy > my:
            my = cy 
            iy = ys_[i]
    return (ix, iy)

t = int(input())
for i in range(1, t+1):
    x, y = sol()
    print('Case #{}: {} {}'.format(i, x, y))

