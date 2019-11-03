'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
'''

from typing import List
class Solution:
    '''
    Idea: dp
    Complexity: O(n^2) in time and space
    '''
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        sol = []
        for i in nums:
            
            arr = max([[]] + [e for e in sol if i % e[-1] == 0], key=lambda u: len(u)).copy()
            arr.append(i)
            sol.append(arr)
        return max(sol, key=lambda u: len(u))