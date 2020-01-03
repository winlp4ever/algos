from typing import List

class Solution:
    '''
    Idea: greedy
    complexity: O(n) time and O(1) space
    '''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        ps = sorted(points)
        h = ps[0][1]
        sol = 1
        for lo, hi in ps[1:]:
            if lo <= h:
                h = min(h, hi)
            else:
                h = hi
                sol += 1
                    
        return sol