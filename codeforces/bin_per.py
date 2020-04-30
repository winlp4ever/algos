T = int(input())
def sol():
    t = input().strip()
    if len(t) <= 2:
        return t
    if '0' not in t or '1' not in t:
        return t
    
    res = ''
    for c in t:
        if c == '0':
            res += c + '1'
        if c == '1':
            res += '0' + c 
    return res

for _ in range(T):
    print(sol())