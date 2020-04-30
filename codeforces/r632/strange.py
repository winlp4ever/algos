t = int(input())

def sol():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1):
        if a[i] + 1 != a[i+1] and a[i] < a[i+1]:
            return False
    return True

for i in range(t):
    print('Yes' if sol() else 'No')