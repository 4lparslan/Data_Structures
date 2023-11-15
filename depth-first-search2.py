def dfs_find_vertex(graph, current, target, visited=None):
    if visited is None:
        visited = set()

    visited.add(current)
    print(f"Processing vertex {current}")

    if current == target:
        print(f"Vertex {target} found!")
        return True

    for neighbor in graph[current] - visited:
        if dfs_find_vertex(graph, neighbor, target, visited):
            return True

    return False

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

start_vertex = 'A'
target_vertex = 'F'
print("DFS Traversal:")
result = dfs_find_vertex(graph, start_vertex, target_vertex)

if not result:
    print(f"Vertex {target_vertex} not found in the graph.")
