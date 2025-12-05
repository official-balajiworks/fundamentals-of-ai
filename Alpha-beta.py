import math

def alphabeta(node, alpha, beta, maximizing):
    value = tree[node]

    # If leaf, return the value
    if isinstance(value, int):
        return value

    # MAX player
    if maximizing:
        best = -math.inf
        for child in value:
            best = max(best, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, best)

            # Prune
            if beta <= alpha:
                print(f"Pruned branch at {node} -> {child} (MAX)")
                break
        return best

    else:
        best = math.inf
        for child in value:
            best = min(best, alphabeta(child, alpha, beta, True))
            beta = min(beta, best)

            # Prune
            if beta <= alpha:
                print(f"Pruned branch at {node} -> {child} (MIN)")
                break
        return best


# Game Tree
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],

    # Leaves
    "D": 3,
    "E": 6,
    "F": 1,
    "G": 0
}

print("=== Alpha-Beta Pruning Trace ===")   

root_value = alphabeta("A", -math.inf, math.inf, True)
print("\nMinimax value of A:", root_value)

# Find best move for MAX
best_move = max(tree["A"], key=lambda c: alphabeta(c, -math.inf, math.inf, False))
best_value = alphabeta(best_move, -math.inf, math.inf, False)

print("\nOptimal Move for MAX:", best_move)
print("Value of that move:", best_value)
