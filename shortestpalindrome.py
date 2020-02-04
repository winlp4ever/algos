def shortestPalin(s_: str):
    s = '#'
    for c in s_:
        s += c 
        s += '#'
    n = len(s)
    rds = [0 for _ in s]
    mid = 0
    rad = 0
    while mid < n-1:
        cn = False
        for i in range(mid + 1, mid + rad + 1):
            r = min(rds[2*mid-i], mid+rad-i)
            rds[i] = r
            if r < mid+rad-i:
                continue 
            if i+r+1 >= n or s[i+r+1] != s[i-r-1]:
                continue
            r += 1
            while i+r+1 < n and i-r-1>=0:
                if s[i+r+1] == s[i-r-1]:
                    r+=1
                else:
                    break
            mid = i
            rad = r 
            rds[i] = r
            cn = True
            break
        if cn:
            continue 
        mid += rad + 1
        rad = 0
        for u in range(mid+1, n):
            if 2*mid - u >= 0 and s[u] == s[2*mid-u]:
                rad += 1
            else:
                break
        if mid < n:
            rds[mid] = rad
    for i in range(n-1,-1,-1):
        if rds[i] == i:
            break
    p = s[-1:i:-1] + s[i:]
    return p[1::2]
if __name__ == '__main__':
    s = 'abcd'
    print(shortestPalin(s))