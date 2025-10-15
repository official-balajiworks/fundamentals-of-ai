from queue import PriorityQueue

# Define the graph as a dictionary
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5},
    'B': {'C': 1, 'D': 3},
    'C': {'D': 2, 'G': 5},
    'D': {'G': 1},
    'G': {}
}

# Define heuristic values (estimated distance to goal)
heuristic = {
    'S': 7, 'A': 6, 'B': 2, 'C': 1, 'D': 1, 'G': 0
}

def a_star_search(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    g_cost = {start: 0}
    came_from = {start: None}

    while not pq.empty():
        f_cost, current = pq.get()

        # If goal reached
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        # Explore neighbors
        for neighbor, cost in graph[current].items():
            new_cost = g_cost[current] + cost
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                pq.put((f_cost, neighbor))
                came_from[neighbor] = current

    return None

# Run A* search
path = a_star_search('S', 'G')
print("Shortest path found by A*:", path)
