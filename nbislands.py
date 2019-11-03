from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        cpn = 0
        flags = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or flags[i][j] >= 0:
                    continue
                visited = [(i, j)]
                while visited:
                    r, c = visited.pop()
                    if r > 0 and grid[r-1][c] == '1' and flags[r-1][c] < 0:
                        visited.append((r-1, c))
                        flags[r-1][c] = cpn
                    if r < m-1 and grid[r+1][c] == '1' and flags[r+1][c] < 0:
                        visited.append((r+1, c))
                        flags[r+1][c] = cpn
                    if c > 0 and grid[r][c-1] == '1' and flags[r][c-1] < 0:
                        visited.append((r, c-1))
                        flags[r][c-1] = cpn
                    if c < n-1 and grid[r][c+1] == '1' and flags[r][c+1] < 0:
                        visited.append((r, c+1))
                        flags[r][c+1] = cpn
                cpn += 1
        return cpn


if __name__ == '__main__':
    map_ = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    sol = Solution()
    print(sol.numIslands(map_))