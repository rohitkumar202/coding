# Graph

Code: [traversal_list.py](../graph/traversal_list.py) · [traversal_matrix.py](../graph/traversal_matrix.py) · [problems/](../graph/problems/)

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

## Problems

| Problem | Pattern | Key trick | Code |
|---|---|---|---|
| Copy graph | DFS | Copy every edge, but recurse only into unvisited nodes. **Hint:** `new_graph` can be the `visited` set (a node is in it exactly when visited) | [copy_graph.py](../graph/problems/copy_graph.py) |
| Count islands | DFS on grid | Run DFS from every unvisited `1` and count the starts. Mark visited by setting the cell to `-1`. Check bounds first (`grid[-1]` wraps), then check `== 1` (not truthy: `-1` is truthy) | [count_island.py](../graph/problems/count_island.py) |
| Bipartite graph | BFS 2-coloring | Color each neighbor the opposite color (`1` / `-1`). A neighbor with the same color means an odd cycle, so not bipartite. `colors` doubles as `visited` (`0` = unvisited). Start a BFS from **every** uncolored node (disconnected graph) | [bi_partite_graph.py](../graph/problems/bi_partite_graph.py) |
| Matrix infection (rotting oranges) | Multi-source BFS on grid | Enqueue all infected cells first. Process one level per second (`for _ in range(len(queue))`). Count healthy cells and loop `while queue and healthy > 0`, else the answer is 1 too high. Healthy left over → `-1` | [matrix_infection.py](../graph/problems/matrix_infection.py) |
