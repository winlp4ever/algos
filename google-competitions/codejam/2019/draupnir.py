import sys 

def sol():
    print(200)
    sys.stdout.flush()
    s = int(input())
    r4 = (s // (2**50)) % (2**7)
    r5 = (s // (2**40)) % (2**7)
    r6 = (s // (2**33)) % (2**7)
    print(50)
    sys.stdout.flush()
    v = int(input())
    v -= r4 * (2 ** (50//4)) + r5 * (2 ** (50//5)) + r6 * (2 ** (50//6))
    r1 = (v // (2**50)) % (2**7)
    r2 = (v // (2**25)) % (2**7)
    r3 = (v // (2**16)) % (2**7)
    print(r1, r2, r3, r4, r5, r6)
    sys.stdout.flush()
    res = int(input())
    return 

t, w = map(int, input().split())
for _ in range(t):
    sol()