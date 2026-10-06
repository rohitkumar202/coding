graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2],
    4: [5, 8],
    5: [4, 6],
    6: [5, 7],
    7: [6, 8],
    8: [4, 7],
}

# 0 = unvisited, 1 = blue, -1 = orange
colors = [0] * len(graph.items())


def coloring(queue, graph):
    """BFS over one connected component; False if two neighbors share a color."""
    while queue:
        node = queue.pop(0)  # O(n) on a list; collections.deque.popleft() is O(1)
        color = colors[node]
        for neighbor in graph[node]:
            # Both ends of an edge have the same color -> odd cycle, not bipartite
            if colors[neighbor] == color:
                return False
            # Uncolored means unvisited, so colors doubles as the visited set
            if colors[neighbor] == 0:
                colors[neighbor] = -color  # neighbor must get the opposite color
                queue.append(neighbor)     # colored before queuing, so never queued twice
            # Remaining case: already has the opposite color -> consistent, nothing to do
    return True


res = True
# Try every node as a start, so disconnected components are also checked
for i in list(graph.keys()):
    if colors[i] == 0:      # not reached by any earlier BFS -> new component
        colors[i] = 1       # starting color is arbitrary; components share no edges
        # 'and' because ALL components must be bipartite; it also skips BFS once res is False
        res = res and coloring([i], graph)

print(res)  # False: nodes 4-5-6-7-8 form a 5-cycle