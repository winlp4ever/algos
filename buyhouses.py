T = int(input())
def case():
    N, B = list(map(int, input().split()))
    As = list(map(int, input().split()))
    As.sort()
    print(As)
    count = 0
    for a in As:
        if B >= a:
            B -= a
            count += 1
    return count
for i in range(T):
    print('#%d: %d' % (i+1, case()))