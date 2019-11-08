'''
link to the problem: https://leetcode.com/problems/non-overlapping-intervals/submissions/
'''
from typing import List
class Solution:
    '''
    complexity: O(nlogn) time, O(1) space
    '''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        count = 0
        intervals.sort(key = lambda x:[x[0], x[1]])
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if self.overlapping(curr, intervals[i]):
                count += 1
                curr = self.update_curr(curr, intervals[i])
            else:
                curr = intervals[i]
        return count
    
    def overlapping(self, a, b):
        return b[0] < a[1] and b[0] >= a[0]

    def update_curr(self, a, b):
        if b[1] < a[1]:
            return b
        return a
