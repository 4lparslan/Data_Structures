from collections import defaultdict, deque

def bfs(graph, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        current_vertex = queue.popleft()

        if current_vertex == target:
            print(f"Vertex {target} found!")
            return

        if current_vertex not in visited:
            print(f"Processing vertex {current_vertex}")
            visited.add(current_vertex)
            queue.extend(neighbor for neighbor in graph[current_vertex] if neighbor not in visited)

    print(f"Vertex {target} not found in the graph.")

# Example Usage:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

start_vertex = 0
target_vertex = 3
bfs(graph, start_vertex, target_vertex)
