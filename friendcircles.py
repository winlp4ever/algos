'''
A problem from _leetcode_, but it's also a Union-Find Data Structure revision
'''

from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        n = len(M)
        parents = [i for i in range(n)]
        ranks = [0 for _ in range(n)]

        def find(i):
            # return root ancestor of i
            if parents[i] == i:
                return i
            r = find(parents[i])
            parents[i] = r 
            return r

        def union(i, j):
            pi, pj = find(i), find(j)
            if pi == pj:
                return
            if ranks[pi] > ranks[pj]:
                parents[pj] = pi 
            elif ranks[pi] < ranks[pj]:
                parents[pi] = pj
            else:
                parents[pi] = pj 
                ranks[pj] += 1
        
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    union(i, j)

        count = 0
        for i, u in enumerate(parents):
            if u == i:
                count += 1
        return count
        



        
        