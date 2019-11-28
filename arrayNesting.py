'''
Problem: A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

 

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
 
'''

from typing import List

class Solution:
    '''
    Complexity: O(n) time and space
    '''
    def arrayNesting(self, nums: List[int]) -> int:
        if not nums:
            return 0
        marked = [0 for _ in nums]
        n = len(nums)
        for i in range(n):
            if marked[i] == 0:
                it = i
                marked[i] = 1
                while nums[it] != i:
                    marked[nums[it]] = marked[it]+1
                    it = nums[it]
        return max(marked)