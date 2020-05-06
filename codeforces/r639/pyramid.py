t = int(input())

def f(a):
    return (3*a+1) * a // 2
def binSearch(u, l, h):
    if l+1 >= h:
        return l
    m = (l + h) // 2
    if f(m) <= u:
        return binSearch(u, m, h)
    return binSearch(u, l, m)

def sol():
    n = int(input())
    res = 0
    while n > 0:
        k = binSearch(n, 0, n)
        if k == 0:
            break
        res += 1 
        n -= f(k)
    return res

for _ in range(t):
    print(sol())