#https://leetcode.com/problems/number-of-islands/submissions/

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore_island(i, j):
            if (i < 0 or i >= len(grid)
                or j < 0 or j >= len(grid[0])
                or grid[i][j] == '0'):
                  return
            grid[i][j] = '0'
            explore_island(i+1, j)
            explore_island(i-1, j)
            explore_island(i, j+1)
            explore_island(i, j-1)

        count = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '1':
                    explore_island(i, j)
                    count += 1
        return count

grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

print(num_islands(grid1))
print(num_islands(grid2))
