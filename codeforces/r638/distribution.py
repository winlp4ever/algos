t = int(input())

def sol():
    n, k = map(int, input().split())
    sr = input().strip()
    s = sorted([c for c in sr])
    if k == 1:
        return ''.join(s)
    if s[k-1] != s[0] or k == n:
        return s[k-1]
    if s[k] == s[n-1]:
        return s[k-1] + s[k] * ((n-1) // k)
    return ''.join(s[k-1:])
    
    

for _ in range(t):
    print(sol())
        


    