'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
'''

from typing import List

class Solution:
    '''
    Idea: sumarray and hashmap
    complexity: O(n) time and space
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        memo = dict()
        sums = [0]
        for u in nums:
            sums.append(sums[-1]+u)
        res = 0
        for s in sums:
            if s-k in memo:
                res += memo[s-k]
            if s not in memo:
                memo[s] = 0
            memo[s] += 1
            
        return res