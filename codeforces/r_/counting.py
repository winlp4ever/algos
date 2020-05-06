def gcd(u, v):
    if u < v:
        return gcd(v, u)
    if v == 0:
        return u
    return gcd(v, u%v)

def case(a, b, ld):
    l, r = map(int, input().split())
    if a % b == 0:
        return 0
    if r < max(a, b):
        return 0
    
    low = l // ld 
    high = r // ld
    raw = (high-low)*a
    raw -= min(l-(low*ld),a)
    raw += min(r-(high*ld)+1, a)
    return r-l+1-raw
    

def sol():
    a, b, q = map(int, input().split())
    if a < b:
        a, b = b, a 
    d = gcd(a, b)
    b_ = b // d 
    ld = b_*a
    res = []
    for _ in range(q):
        res.append(str(case(a, b, ld)))
    return res

t = int(input())
for _ in range(t):
    print(' '.join(sol()))