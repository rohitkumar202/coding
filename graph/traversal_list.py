from collections import deque

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [4],
    3: [5],
    4: [5],
    5: [],
}

# DFS implementation
# Print node after the visited check, so each node prints once.
# print(neighbor) in the loop runs before that check: it repeats 4 and 5
# (two paths reach each) and never prints the start node 0.
def dfs(node, graph, visited):
  if node not in visited:    
    print(node)
    visited.add(node)  # mark before recursing, else a cycle loops forever
    for neighbor in graph[node]:            
      dfs(neighbor, graph, visited)
      


# BFS implementation
# Mark nodes when enqueued (not when popped), so each node enters the queue once.
def bfs(queue, graph, visited):
  queue = deque(queue)  # popleft() is O(1); list.pop(0) is O(n)
  visited.update(queue)  # start nodes count as seen
  while queue:
    node = queue.popleft()
    print(node)
    for neighbor in graph[node]:
      if neighbor not in visited:  # skip nodes already queued or processed
        visited.add(neighbor)
        queue.append(neighbor)


if __name__ == "__main__":
  visited = set()
  # dfs(0, graph, visited)
  bfs([0], graph, visited)
