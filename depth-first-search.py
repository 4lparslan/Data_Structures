# We put every node's adjacents in a stack

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)

    return visited

# Example usage:
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B', 'H'},
    'F': {'C'},
    'G': {'C'},
    'H': {'E'}
}

print("DFS Traversal:")
dfs(graph, 'A')
