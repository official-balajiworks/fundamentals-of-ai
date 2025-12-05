import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'E': 1},
    'D': {'B': 5, 'E': 3},
    'E': {'C': 1, 'D': 3}
}

h = {'A': 4, 'B': 3, 'C': 1, 'D': 2, 'E': 0}
def astar(start, goal):
    pq = [(h[start], start)]          # (f, node)
    g = {n: float('inf') for n in graph}
    g[start] = 0
    parent = {start: None}
    while pq:
        _, node = heapq.heappop(pq)
        """ This removes the smallest f(n) value node from priority queue."""
        if node == goal:
            break
        for nb, w in graph[node].items():
            ng = g[node] + w
            if ng < g[nb]:
                g[nb] = ng
                parent[nb] = node
                heapq.heappush(pq, (ng + h[nb], nb))
    # reconstruct path
    path = []
    n = goal
    while n:
        path.append(n)
        n = parent[n]
    return path[::-1], g[goal]
path, cost = astar('A', 'E')
print("Optimal Path:", " -> ".join(path))
print("Total Path Cost:", cost)
