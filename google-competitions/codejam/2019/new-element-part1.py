def gcd(a, b):
    if a == 0:
        return b 
    if b == 0:
        return a
    if b > a:
        return gcd(b, a)
    return gcd(b, a%b)

def sol():
    n = int(input())
    mols = []
    for _ in range(n):
        mols.append(list(map(int, input().split())))
    mols.sort()
    ratios = set()
    for i in range(n):
        for j in range(n):
            if i == j:
                continue 
            ci, di = mols[i]
            cj, dj = mols[j]
            if (ci-cj)*(di-dj) < 0:
                ui = ci - cj
                vi = dj - di
                if ui < 0:
                    ui, vi = -ui, -vi
                g = gcd(ui, vi)
                ui //= g 
                vi //= g 
                ratios.add((ui, vi))
                
    return len(ratios) + 1

t = int(input())
for i in range(1, t+1):
    print('Case #{}: {}'.format(i, sol()))
    