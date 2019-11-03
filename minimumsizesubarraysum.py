'''problem: 
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''
from typing import List

class Solution:
    '''Complexity: O(n) time and space
    '''
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums) < s:
            return 0
        n = len(nums)
        mn = n
        lo = hi = 0
        sm = 0
        while hi < n:
            sm += nums[hi]
            while sm >= s:
                if mn > hi-lo+1:
                    mn = hi-lo+1
                lo += 1
                sm -= nums[lo-1]
            hi += 1
        return mn