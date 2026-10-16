grid = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1],
]

# Brute force: DFS from every cell, moving only to strictly larger neighbors.
# Strictly increasing means a path can never revisit a cell, so no visited set is needed.
# Exponential: the same cell is re-explored from every path that reaches it.
def lip(r, c, prev, grid):
    if not 0 <= r < len(grid):
        return 0
    if not 0 <= c < len(grid[0]):
        return 0    
    if grid[r][c] <= prev:  # must be strictly larger than the previous cell
        return 0
    
    return max(lip(r+1,c, grid[r][c], grid), 
               lip(r-1,c, grid[r][c], grid), 
               lip(r,c+1, grid[r][c], grid), 
               lip(r,c-1,  grid[r][c], grid)) + 1  # +1 for this cell
    

_max = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        _max = max(_max, lip(i,j,-1, grid))
                   
print(_max)  # brute force


# Memoized: memo[(r, c)] = longest increasing path STARTING at (r, c).
# NOTE: that value doesn't depend on how we reached (r, c), so it can be cached.
#       Each cell is computed once -> O(R * C) time and space.
def lip_memo(r, c, grid, memo):
    if (r, c) in memo:
        return memo[(r, c)]
    best = 1  # the path containing just this cell
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] > grid[r][c]:
            best = max(best, 1 + lip_memo(nr, nc, grid, memo))
    memo[(r, c)] = best
    return best


memo = {}  # shared across all starts, so later starts reuse earlier results
print(max(lip_memo(i, j, grid, memo) for i in range(len(grid)) for j in range(len(grid[0]))))  # memoized
