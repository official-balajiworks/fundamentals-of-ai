def resolve(C1, C2):
    for a in C1:
        comp = a[1:] if a.startswith("¬") else "¬"+a
        if comp in C2:
            return (C1 | C2) - {a, comp}
    return None

def resolution(KB):
    KB = [set(c) for c in KB]
    while True:
        new = []
        for i in range(len(KB)):
            for j in range(i+1, len(KB)):
                r = resolve(KB[i], KB[j])
                if r is not None:
                    if len(r) == 0: return True   # empty clause found
                    new.append(r)
        if all(n in KB for n in new): return False  # no progress
        KB += new

# ------------ EXAMPLE ------------
# From: {¬P, Q}, {P} derive Q
KB = [
    {"¬P", "Q"},
    {"P"}
]

print("Entails?", resolution(KB))
