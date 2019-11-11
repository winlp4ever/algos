'''Problem:
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 '''

from typing import List
from collections import deque
class Solution:
    '''
    Complexity: O(m*n) time and space
    Idea: breadth first search (a bit twist at the beginning at we add all 0s points to the initial queue)
    '''
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        memo = [[10000 for _ in range(n)] for _ in range(m)]
        Q = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    memo[i][j] = 0
                    Q.appendleft([i, j, 0])

        while Q:
            u, v, h = Q.pop()
            if u > 0 and memo[u-1][v] == 10000:
                memo[u-1][v] = h+1
                Q.appendleft([u-1, v, h+1])
            if v > 0 and memo[u][v-1] == 10000:
                memo[u][v-1] = h+1
                Q.appendleft([u, v-1, h+1])
            if u < m-1 and memo[u+1][v] == 10000:
                memo[u+1][v] = h+1
                Q.appendleft([u+1, v, h+1])
            if v < n-1 and memo[u][v+1] == 10000:
                memo[u][v+1] = h+1
                Q.appendleft([u, v+1, h+1])

        return memo
