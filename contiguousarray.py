'''
Problem:
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''
from typing import List 

class Solution:
    '''
    Complexity: O(n) time and space
    Idea: count array: records the difference in nb between 0s and 1s. Choose largest distance between two cells of same value
    '''
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        diffs = [0]
        for e in nums:
            if e == 0:
                diffs.append(diffs[-1] - 1)
            else:
                diffs.append(diffs[-1] + 1)
        memo = dict()
        for i, u in enumerate(diffs):
            if u not in memo:
                memo[u] = []
            memo[u].append(i)
        mxs = [v[-1] - v[0] for _, v in memo.items()]
        return max(mxs)