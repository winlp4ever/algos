from typing import List

class Solution:
    '''
    Link to problem:https://leetcode.com/problems/queue-reconstruction-by-height/
    Complexity: O(n^2)
    '''
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        people.sort(key=lambda u: (u[0], -u[1]), reverse=True)
        Q = []
        for h, k in people:
            Q.insert(k, [h, k])
        return Q