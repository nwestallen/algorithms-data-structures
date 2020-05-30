def count_islands(grid):
    def explore_island(i,j):
        if (i < 0 or i >= len(grid)
           or j < 0 or j >= len(grid[0])
           or grid[i][j] == 0):
            return
        grid[i][j] = 0
        explore_island(i+1, j)
        explore_island(i-1, j)
        explore_island(i, j+1)
        explore_island(i, j-1)

    count = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                explore_island(i, j)
                count += 1
    return count

grid = [[1,0,1,0],
        [1,0,1,0],
        [0,0,1,0]]

print(count_islands(grid))