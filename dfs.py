graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 
    'E': [], 
    'F': []
}

visited = []

def b(node):
    visited.append(node)
    for nei in graph[node]:
        if nei not in visited:
            b(nei)

b('A')

print("Traversal:", visited)
print("Path to F exists?", 'F' in visited)
