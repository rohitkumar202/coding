# Word ladder: each word is a node, and an edge joins words that differ by one letter.
graph = {
    'red': ['bed', 'rod', 'rad'],
    'bed': ['red', 'bad'],
    'hat': ['rat', 'hit', 'bat'],
    'rod': ['red', 'rad'],
    'rad': ['red', 'rod', 'rat', 'bad'],
    'rat': ['hat', 'rad', 'bat'],
    'hit': ['hat'],
    'bad': ['bed', 'rad', 'bat'],
    'bat': ['hat', 'rat', 'bad'],
}

# Shortest transformation = BFS level by level; the answer is the number of words
# in the path (levels), counting the start word.
def level_order_traversal(queue, graph, visited, end, count = 0):
    while queue:
        count = count + 1  # one level = one more word in the sequence
        for _ in range(len(queue)):  # process exactly one level
            node = queue.pop(0)
            if end == node:
                return count  # BFS reaches end first by the shortest path
            visited.add(node)  # only needed for the start word; the rest are marked on enqueue

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)  # mark on enqueue, so a word is queued once
    # Loop ended without popping end -> unreachable, so return 0 (word ladder convention).
    # NOTE: this check is always true here (a reached end returns inside the loop),
    #       so `return count` never runs. A plain `return 0` does the same.
    if end not in visited:
        return 0
    return count # this is not requried as code will never reach here


res = level_order_traversal(['red'], graph, set(), 'zzz')
print(res)

