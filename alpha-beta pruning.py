def alphabeta(node, depth, alpha, beta, maximizing, tree):
    if depth == 0 or node not in tree:
        return node                 # leaf value

    if maximizing:
        v = -999
        for c in tree[node]:
            v = max(v, alphabeta(c, depth-1, alpha, beta, False, tree))
            alpha = max(alpha, v)
            if beta <= alpha: break
        return v
    else:
        v = 999
        for c in tree[node]:
            v = min(v, alphabeta(c, depth-1, alpha, beta, True, tree))
            beta = min(beta, v)
            if beta <= alpha: break
        return v

# ---------- Example Game Tree ----------
# Leaf nodes = their utility value
tree = {
    "A": ["B","C"],
    "B": [3, 5],
    "C": [2, 9]
}

print("Best value:", alphabeta("A", 3, -999, 999, True, tree))
