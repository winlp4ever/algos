t = int(input())

def sol():
    n, a, b, c, d = map(int, input().split())
    return (a-b)*n <= c+d and  (a+b)*n >=c-d

for i in range(t):
    if sol():
        print('Yes')
    else: 
        print('No')