t = int(input())

def ord2(k):
    i = 0
    while k:
        k //= 2
        i += 1
    return i

def binsearch(nums, val, l, h):
    if nums[h] <= val:
        return h
    if nums[0] > val:
        return -1
    if l + 1 >= h:
        return l
    m = (l+h)//2
    if val >= nums[m]:
        return binsearch(nums, val, m, h)
    return binsearch(nums, val, l, m)
    

def sol():
    n = int(input())
    k = ord2(n)
    # days = k-1
    nbs = []
    i = 1
    pw2 = 0
    while pw2 < k-1:
        nbs.append(i)
        i *= 2
        pw2 += 1
    
    d = n+1-i
    ix = binsearch(nbs, d, 0, k-2)
    nbs.insert(ix+1, d)
    res = []
    for i in range(1, k):
        res.append(str(nbs[i]-nbs[i-1]))
    return '%d\n%s' % (k-1, ' '.join(res))

for _ in range(t):
    print(sol())
     
    
    