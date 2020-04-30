import heapq
import math


T = int(input())


def case():
    # input
    n, k = list(map(int, input().split()))
    sessions = list(map(int, input().split()))

    # solution
    diffs = []
    for i in range(n-1):
        diffs.append(sessions[i+1] - sessions[i])
        
    def optimal_i(d):
        return sum([int(math.ceil(d_/d))-1 for d_ in diffs])
    
    if optimal_i(1) <= k:
        return 1

    dmx = max(*diffs)
    def bin_search(l, h):
        if l >= h-1:
            return h
        m = (l+h) // 2
        if optimal_i(m) <= k:
            return bin_search(l, m)
        return bin_search(m, h)
    return bin_search(1, dmx)


for j in range(1, T+1):
    print('Case #{}: {}'.format(j, case()))