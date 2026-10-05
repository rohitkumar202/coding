graph = {
    0: [1, 2],
    1: [3, 4],
    2: [4],
    3: [5],
    4: [5],
    5: [],
}

# Copy graph: DFS from `node`, adding each node and its edges to new_graph.
# Only nodes reachable from the start node get copied.
# NOTE: `visited` isn't needed. Use `new_graph` as visited instead:
#       `if node not in new_graph:`, since a node is in new_graph exactly when visited.
def copy_graph(graph, node, visited, new_graph):
    if node not in visited:
        # print(node)
        if node not in new_graph:
            new_graph[node] = []  # create the node before adding its edges
        
        visited.add(node)  # mark before recursing, else a cycle loops forever
        for neighbor in graph[node]:
            new_graph[node].append(neighbor)  # copy every edge, even to visited nodes
            copy_graph(graph, neighbor, visited, new_graph)

        return new_graph  # only the top-level call's return value is used

    

if __name__ == "__main__":
    visited = set()
    new_graph = {}
    new_graph = copy_graph(graph, 0, visited, new_graph)
    print(graph)
    print(new_graph)
