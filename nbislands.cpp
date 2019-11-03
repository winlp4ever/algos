#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        typedef pair<int, int> P;
        int m = grid.size();
        int n = grid[0].size();
        char cpn = 1;
        vector<vector<int>> flags;
        for (int i = 0; i < m; i++) {
            vector<int> row;
            for (int j = 0; j < n; j++) {
                row.push_back(0);
            }
            flags.push_back(row);
        }
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (flags[i][j] > 0 || grid[i][j] == '0')
                    continue;
                queue<P> visited;
                visited.push(P(i, j));
                while (!visited.empty()) {
                    P v = visited.front();
                    int r, c;
                    r = v.first;
                    c = v.second;
                    visited.pop();
                    if (r > 0 && grid[r-1][c] == '1' && flags[r-1][c] == 0) {
                        visited.push(P(r-1, c));
                        flags[r-1][c] = cpn;
                    }
                    if (r < m-1 && grid[r+1][c] == '1' && flags[r+1][c] == 0) {
                        visited.push(P(r+1, c));
                        flags[r+1][c] = cpn;
                    }
                    if (c > 0 && grid[r][c-1] == '1' && flags[r][c-1] == 0) {
                        visited.push(P(r, c-1));
                        flags[r][c-1] = cpn;
                    }
                    if (c < n-1 && grid[r][c+1] == '1' && flags[r][c+1] == 0) {
                        visited.push(P(r, c+1));
                        flags[r][c+1] = cpn;
                    }
                }
                cpn ++;
            }
        return cpn-1;
    }
};