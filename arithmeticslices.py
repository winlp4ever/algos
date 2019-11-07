from typing import List

class Solution:
    '''
    complexity: O(n^2) time and O(n) space
    idea: dynamic programming
    link to problem: https://leetcode.com/problems/arithmetic-slices/
    '''
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        n = len(A)
        def isArith(a):
            return a[2]-a[1] if a[2]-a[1] == a[1]-a[0] else 10000
        regis = [isArith(A[i:i+3]) for i in range(n-2)]
        res = sum([1 if e < 10000 else 0 for e in regis])
        for i in range(3, n):
            for j in range(n-i):
                if regis[j] < 10000 and A[j+i] - A[j+i-1] == regis[j]:
                    
                    res += 1
                else:
                    regis[j] = 10000
        return res