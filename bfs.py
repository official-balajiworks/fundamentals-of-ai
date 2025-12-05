from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph.get(node, []))

graph_input = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G']
}

bfs(graph_input, 'A')
