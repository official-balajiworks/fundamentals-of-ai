import random

def conflicts(state, col):
    row = state[col]
    return sum(state[c] == row or abs(state[c]-row)==abs(c-col)
               for c in range(len(state)) if c != col)

def min_conflict_value(state, col, n):
    return min(range(n), key=lambda r: 
               sum(r == state[c] or abs(r-state[c])==abs(c-col)
                   for c in range(len(state)) if c != col))

def min_conflicts(n, steps=10000):
    state = [random.randrange(n) for _ in range(n)]
    for _ in range(steps):
        bad = [c for c in range(n) if conflicts(state, c)]
        if not bad: return state
        col = random.choice(bad)
        state[col] = min_conflict_value(state, col, n)
    return None

# ---------- Example: Solve 8-Queens ----------
sol = min_conflicts(8)
print("Solution:", sol)
