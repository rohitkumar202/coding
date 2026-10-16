# this matrix_infection proble is same as rotton oranges

grid = [
    [2, 1, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 1, 2],
    [0, 0, 1, 1, 1],
]


queue = []
seconds = 0
healthy = 0

# Multi-source BFS: start from every infected cell at once; each BFS level is 1 second.
def infect(queue, grid):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    global healthy
    # NOTE: `healthy > 0` is needed. Without it, the loop runs one extra round after
    #       the last infection and the answer comes out 1 second too high.
    while queue and healthy > 0:
        for _ in range(len(queue)):  # process exactly one level (one second)
            i,j = queue.pop(0)        
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2  # infect on enqueue, so a cell is queued once
                        healthy -= 1
                        queue.append((ni, nj))
        global seconds            
        seconds += 1

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 2:
            queue.append((i,j))
        if grid[i][j] == 1:
            healthy +=1

infect(queue, grid)

if healthy > 0:  # some healthy cell is unreachable
    print(-1)

if healthy == 0:
    print('seconds: ', seconds)







