grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
]

# Count islands: each DFS sinks one whole island, so count the DFS starts.
def dfs(row, col, grid):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left (no diagonals)
    grid[row][col] = -1  # mark visited in place, so no visited set is needed

    for d in dirs:
        new_row = row + d[0]
        new_col = col + d[1]
        # Bounds check first: Python's grid[-1] wraps to the last row instead of failing.
        if new_row >=0 and new_row < len(grid) and new_col >=0 and new_col < len(grid[0]):
            # NOTE: must be `== 1` (unvisited land). Visited cells are -1, which is truthy,
            #       so `if grid[r][c]:` or `!= 0` recurses into visited cells forever.
            if grid[new_row][new_col] == 1:
                dfs(new_row, new_col, grid)
            
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:  # unvisited land starts a new island
            dfs(i, j, grid)
            count = count + 1


print(count)
