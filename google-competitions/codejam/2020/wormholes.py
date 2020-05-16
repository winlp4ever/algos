def gcd(a, b):
    if a < 0:
        a = -a 
    if b < 0:
        b = -b
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a%b)

def sol():
    n = int(input())
    points = []
    for _ in range(n):
        points.append(list(map(int, input().split())))
    dirs = dict()
    ax = set()
    ay = set()
    for i in range(n):
        xi, yi = points[i]
        for j in range(i+1, n):
            xj, yj = points[j]
            if xi == xj:
                ay.add((xi, yi))
                ay.add((xj, yj))
            elif yi == yj:
                ax.add((xi, yi))
                ax.add((xj, yj))
            else:
                d = gcd(xi-xj, yi-yj)
                a, b = (xi-xj)//d, (yi-yj)//d
                if a < 0:
                    a, b = -a, -b 
                if (a, b) not in dirs:
                    dirs[(a, b)] = set()
                dirs[(a, b)].add((xi, yi))
                dirs[(a, b)].add((xj, yj))
    k = max(*[len(u) for k, u in dirs.items()], len(ax), len(ay)) 
    if k % 2 == 0:
        return min(k+2, n)  
    return min(k+1, n)
    


t = int(input())

for i in range(1, t+1):
    print('Case #{}: {}'.format(i, sol()))
    