from collections import deque
def bfs(graph,start_node):
    visited=set()
    queue=deque()
    queue.append(start_node)
    visited.add(start_node)
    print("BFS Traversal Order:")
    while queue :
        current_node=queue.popleft()
        print(current_node,end=' ') 
        for neighbor in graph.get(current_node,[]):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
graph_input={
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G']
}

bfs(graph_input,'A')