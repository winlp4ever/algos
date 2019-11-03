'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''
from typing import List
class Solution:
    def canFinish(self, n: int, pres: List[List[int]]) -> bool:
        if n == 0:
            return True
        graph = [[] for _ in range(n)]
        for u, v in pres:
            graph[u].append(v)
        marked = [-1 for _ in range(n)]
        
        def foo(memo, u):
            marked[u] = 0
            if u in memo:
                return False
            memo.add(u)
            for adj in graph[u]:
                if not foo(memo, adj):
                    return False
            memo.remove(u)
            return True
            
        for i in range(n):
            if marked[i] >= 0:
                continue
            if not foo(set(), i):
                return False
        return True