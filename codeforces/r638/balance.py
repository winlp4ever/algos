t = int(input())

def pow2(k):
    if k == 0:
        return 1
    u = pow2(k//2)
    if k%2:
        return u*u*2
    return u*u

def sol():
    n = int(input())
    return 2*pow2(n//2)-2

for _ in range(t):
    print(sol())