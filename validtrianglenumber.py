'''
Problem:https://leetcode.com/problems/valid-triangle-number/
'''
from typing import List
class Solution:
    '''
    Complexity: O(n^2) time, O(log n) space
    '''
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        sol = 0
        for i in range(n-2):
            if nums[i] == 0:
                continue
            k = i+2
            for j in range(i+1, n-1):
                while k < n and nums[k] < nums[i] + nums[j]:
                    k += 1
                sol += k-j-1
        return sol