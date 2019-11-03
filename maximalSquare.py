from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        matrix = [[int(u) for u in r] for r in matrix]
        m = len(matrix)
        n = len(matrix[0])
        mx = 0
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0 and matrix[i][j] > 0:
                    u = min(matrix[i-1][j], matrix[i][j-1])
                    matrix[i][j] = u+1 if matrix[i-u][j-u] > 0 else u
                if mx < matrix[i][j]:
                    mx = matrix[i][j]
        return mx**2