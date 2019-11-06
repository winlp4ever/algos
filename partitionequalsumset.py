'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        sm = sum(nums)
        if sm % 2:
            return False
        tgt = sm//2
        n = len(nums)
        dp = set()
        def rec(i, s):
            if (i, s) in dp or s > tgt:
                dp.add((i, s))
                return False
            if s == tgt:
                return True
            for j in range(i+1, n):
                if rec(j, s + nums[j]):
                    return True
            dp.add((i, s))
            return False
        return rec(0, 0)
            