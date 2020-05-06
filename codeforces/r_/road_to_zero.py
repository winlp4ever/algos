def sol():
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if 2*a < b:
        return max(x-1, 0) * a + max(y-1, 0) * a + (x > 0 and y > 0) * b + (x == 0 or y == 0) * a
        #return (x+y)*a
    return abs(x-y) * a + min(x, y) * b 

t = int(input())
for _ in range(t):
    print(sol())
