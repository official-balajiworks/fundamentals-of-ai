import functools 
import math
def alphabeta(node, alpha, beta, maximizing):
    value = tree[node]
    # If leaf → return
    if isinstance(value, int):
        return value
    if maximizing:
        best = -math.inf
        for child in value:
            best = max(best, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned branch at {node} -> {child} (MAX)")
                break
        return best
    else:
        best = math.inf
        for child in value:
            best = min(best, alphabeta(child, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned branch at {node} -> {child} (MIN)")
                break
        return best
tree = {
    'A': ['B', 'C'],
    'B': ['B1', 'B2', 'B3'],
    'C': ['C1', 'C2'],
    'B1': 3, 'B2': 5, 'B3': 6,
    'C1': 1, 'C2': 2
}
print("=== Alpha-Beta Pruning Trace ===")
root_value = alphabeta('A', -math.inf, math.inf, True)
print("\nMinimax value of A:", root_value)
# Pick best move for MAX
best_move = max(tree['A'], key=lambda c: alphabeta(c, -math.inf, math.inf, False))
best_value = alphabeta(best_move, -math.inf, math.inf, False)
print("Optimal Move for MAX:", best_move)
print("Value of that move:", best_value)
