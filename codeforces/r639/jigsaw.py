t = int(input())

def sol():
    m, n = map(int, input().split())
    if m == 1 or n == 1:
        return True
    if m == 2 and n == 2:
        return True
    return False 

for _ in range(t):
    print('YES' if sol() else 'NO')
    