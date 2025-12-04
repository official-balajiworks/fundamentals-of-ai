from collections import deque

def applicable(state, pre):
    return all(p in state for p in pre)

def apply(state, add, delete):
    return (state | set(add)) - set(delete)

def plan(initial, goal, actions):
    q = deque([(initial, [])])
    seen = {tuple(sorted(initial))}

    while q:
        state, steps = q.popleft()

        if all(g in state for g in goal):
            return steps

        for name, pre, add, delete in actions:
            if applicable(state, pre):
                new_state = apply(state, add, delete)
                key = tuple(sorted(new_state))
                if key not in seen:
                    seen.add(key)
                    q.append((new_state, steps + [name]))

    return None

# ---------- EXAMPLE ----------
initial = {"hungry"}
goal = {"not_hungry"}

actions = [
    ("cook", ["hungry"], ["food"], []),
    ("eat", ["food"], ["not_hungry"], ["hungry"]),
]

print(plan(initial, goal, actions))
