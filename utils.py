def search(a, val):
    '''
    binary search: given an inscreasing array and a value val: return index of least element larger or equal to val
    '''
    if not a or a[-1] < val:
        return -1
    if a[0] >= val:
        return 0
    def binSearch(lo, hi):
        if lo+1 >= hi:
            return hi
        mi = (lo+hi) // 2
        if a[mi] < val:
            return binSearch(mi, hi)
        return binSearch(lo, mi) 
    return binSearch(0, len(a)-1)