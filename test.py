def foo(l, k: int) -> int:
    # longest contiguous subseq whose sum infe or equal to k
    
    i = 0
    j = 0
    lg = 0
    sm = 0
    n = len(l)
    while j < n:
        sm += l[j]
        while sm > k:
            sm -= l[i]
            i += 1
        if j-i+1 > lg:
            lg = j-i+1
        j += 1
        
    return lg

a = []
k = 8
print(foo(a, k))