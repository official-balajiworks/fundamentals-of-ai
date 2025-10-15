from queue import PriorityQueue

def greedy_best_first_search(graph, heuristics, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start))  # (h(n), node)
    parent = {start: None}
    
    while not pq.empty():
        h, node = pq.get()
        if node in visited:
            continue
        print(f"Visiting: {node} (h={h})")
        visited.add(node)
        
        if node == goal:
            print("Goal found!")
            break
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                pq.put((heuristics[neighbor], neighbor))
                parent[neighbor] = node
    
    # Reconstruct path
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = parent.get(curr)
    path.reverse()
    return path

# Example graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

# Heuristic values
heuristics = {
    'A': 8, 'B': 6, 'C': 4, 'D': 5, 'E': 3, 'F': 2, 'G': 1, 'H': 0
}

# Run the algorithm
path = greedy_best_first_search(graph, heuristics, 'A', 'H')
print("\nPath found:", " → ".join(path))
