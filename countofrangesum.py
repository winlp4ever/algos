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
    def cRsPos(self, nums, lower, upper):
        '''
        if the array contains only positive integers, then the complexity will be instead O(n) time and O(1) space
        '''
        if not nums:
            return 0
        lo = hi = 0
        sm_lo = sm_hi = nums[0]
        n = len(nums)
        res = 0
        for i, u in enumerate(nums):
            if lo < i:
                lo = i 
            if hi < i:
                hi = i
            while hi < n-1 and sm_hi <= upper:
                hi += 1
                sm_hi += nums[hi]
            
            while lo < n-1 and sm_lo < lower:
                lo += 1
                sm_lo += nums[lo]
            res += hi - lo
            if sm_hi <= upper:
                res += 1
            print(lo, hi)
            sm_hi -= u
            sm_lo -= u
        return res
            
if __name__ == '__main__':
    a = [1, 4, 6]
    l = 3
    h = 8
    sol = Solution()
    print(sol.cRsPos(a, l, h))