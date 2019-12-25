import heapq
from typing import List
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        s = 0
        Q = []
        for i in range(1, m-1):
            heapq.heappush(Q, (heightMap[i][0], i, 0))
            heapq.heappush(Q, (heightMap[i][n-1], i, n-1))
            heightMap[i][0] = -1
            heightMap[i][n-1] = -1
        for j in range(1, n-1):
            heapq.heappush(Q, (heightMap[0][j], 0, j))
            heapq.heappush(Q, (heightMap[m-1][j], m-1, j))
            heightMap[0][j] = -1
            heightMap[m-1][j] = -1
        min_ = Q[0][0]
        heightMap[0][0] = -1
        heightMap[m-1][0] = -1
        heightMap[m-1][n-1] = -1
        heightMap[0][n-1] = -1

        while Q:
            _, y, x = heapq.heappop(Q)
            if y-1 >= 0 and heightMap[y-1][x] > -1:
                heapq.heappush(Q, (heightMap[y-1][x], y-1, x))
                s += max(min_, heightMap[y-1][x]) - heightMap[y-1][x]
                heightMap[y-1][x] = -1
            if y+1 < m and heightMap[y+1][x] > -1:
                heapq.heappush(Q, (heightMap[y+1][x], y+1, x))
                s += max(min_, heightMap[y+1][x]) - heightMap[y+1][x]
                heightMap[y+1][x] = -1
            if x-1 >= 0 and heightMap[y][x-1] > -1:
                heapq.heappush(Q, (heightMap[y][x-1], y, x-1))
                s += max(min_, heightMap[y][x-1]) - heightMap[y][x-1]
                heightMap[y][x-1] = -1
            if x+1 < n and heightMap[y][x+1] > -1:
                heapq.heappush(Q, (heightMap[y][x+1], y, x+1))
                s += max(min_, heightMap[y][x+1]) - heightMap[y][x+1]
                heightMap[y][x+1] = -1
            if Q and min_ < Q[0][0]:
                min_ = Q[0][0]
        return s