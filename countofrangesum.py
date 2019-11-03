from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0
        sm = [0]
        for ele in nums:
            sm.append(sm[-1]+ele)
        n = len(sm)
        
        def mergeSort(lo, hi):
            if lo == hi:
                return 0
            mi = (lo+hi) // 2
            count = mergeSort(lo, mi) + mergeSort(mi+1, hi)
            l = r = mi+1
            for i in range(lo, mi+1):
                while l < hi+1 and sm[l] - sm[i] < lower:
                    l += 1
                while r < hi+1 and sm[r] - sm[i] <= upper:
                    r += 1
                count += r-l
                
            # merge
            tmp = []
            j = lo
            for i in range(mi+1, hi+1):
                while j < mi+1 and sm[j] < sm[i]:
                    tmp.append(sm[j])
                    j += 1
                tmp.append(sm[i])
            tmp += sm[j: mi+1]            
            sm[lo:hi+1] = tmp
            return count
        count = mergeSort(0,n-1)
        return count