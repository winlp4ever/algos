import sys

L = 10 ** 9

t, a, b = map(int, input().split())
def search(l, h, ax, begin, cnt):
    if cnt:
        return
    if l+1 >= h:
        if begin:
            return l
        else:
            return h
    mi = (l + h) // 2
    
    if ax:
        print(mi, 0)
    else:
        print(0, mi)
    sys.stdout.flush()
    s = input()
    if s == 'MISS':
        if begin:
            return search(mi, h, ax, begin, cnt)
        else:
            return search(l, mi, ax, begin, cnt)
    if s == 'HIT':
        if begin:
            return search(l, mi, ax, begin, cnt)
        else:
            return search(mi, h, ax, begin, cnt)
    if s == 'CENTER':
        if ax:
            cnt = [mi, 0]
        else:
            cnt = [0, mi]
        return

def sol():
    cnt = []
    ux = search(-L, 0, True, True, cnt)
    vx = search(0, L, True, False, cnt)
    uy = search(-L, 0, False, True, cnt)
    vy = search(0, L, False, False, cnt)
    if cnt:
        return 0
    else:
        print((ux+vx) // 2, (uy+vy) // 2)
        verd = input()
        if verd != 'CENTER':
            return -1
        return 0

for _ in range(t):
    if sol() == -1:
        break
