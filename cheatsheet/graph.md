# Graph

Code: [traversal_list.py](../graph/traversal_list.py) · [traversal_matrix.py](../graph/traversal_matrix.py)

## Important points

- Keep a `visited` set of **nodes**, not edges. Graphs can have cycles.
- DFS (recursive): mark visited **on entry**, before recursing.
- BFS: mark visited **on enqueue**, not on pop.
- Iterative DFS with a stack: mark on **pop**.
- In BFS, use `deque.popleft()` (O(1)), not `list.pop(0)` (O(n)).
- BFS gives the shortest path in an unweighted graph. DFS doesn't.
- Time: O(V + E) with an adjacency list, O(V²) with a matrix.
- Disconnected graph: start a traversal from every unvisited node.
- List vs matrix: only the neighbor loop changes.

## DFS

**Adjacency list**
```python
def dfs(node, graph, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for nb in graph[node]:
            dfs(nb, graph, visited)
```

**Adjacency matrix**
```python
def dfs(node, graph, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for nb in range(len(graph)):
            if graph[node][nb] == 1:
                dfs(nb, graph, visited)
```

## BFS

**Adjacency list**
```python
def bfs(start, graph):
    queue, visited = deque([start]), {start}
    while queue:
        node = queue.popleft()
        print(node)
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
```

**Adjacency matrix**
```python
def bfs(start, graph):
    queue, visited = deque([start]), {start}
    while queue:
        node = queue.popleft()
        print(node)
        for nb in range(len(graph)):
            if graph[node][nb] == 1 and nb not in visited:
                visited.add(nb)
                queue.append(nb)
```
