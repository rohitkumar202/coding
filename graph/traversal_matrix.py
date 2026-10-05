from collections import deque

graph = [
    # 0  1  2  3  4  5
    [0, 1, 1, 0, 0, 0],  # 0
    [0, 0, 0, 1, 1, 0],  # 1
    [0, 0, 0, 0, 1, 0],  # 2
    [0, 0, 0, 0, 0, 1],  # 3
    [0, 0, 0, 0, 0, 1],  # 4
    [0, 0, 0, 0, 0, 0],  # 5
]

def dfs(node, graph, visited):
    print(node)
    visited.add(node)

    for j in range(len(graph[node])):
        if graph[node][j] == 1 and j not in visited:            
            dfs(j, graph, visited)
           
        


# BFS implementation
# Mark nodes when enqueued (not when popped), so each node enters the queue once.
def bfs(queue, graph, visited):
    queue = deque(queue)  # popleft() is O(1); list.pop(0) is O(n)
    visited.update(queue)  # start nodes count as seen
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in range(len(graph[node])):
            if graph[node][neighbor] == 1 and neighbor not in visited:  # edge exists and not yet queued
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == "__main__":
    visited = set()
    # dfs(0, graph, visited)
    bfs([0], graph, visited)