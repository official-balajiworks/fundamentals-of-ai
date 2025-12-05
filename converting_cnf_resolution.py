import itertools

# Variables
vars = ['A','B','C','D','E','F','G']

# Implication helper
imp = lambda p, q: (not p) or q

# KB truth check
def KB(a):
    A,B,C,D,E,F,G = a['A'],a['B'],a['C'],a['D'],a['E'],a['F'],a['G']
    return (
        imp(A or B, C) and
        imp(C, D and E) and
        ((not A) or F) and
        ((not F) or (not B)) and
        imp(E, G)
    )

# ---------- Truth Table Entailment ----------
def truth_entails():
    for combo in itertools.product([False,True], repeat=7):
        a = dict(zip(vars, combo))
        if KB(a) and not a['G']:
            print("Counterexample:", a)
            return False
    return True

# ---------- CNF Resolution ----------
clauses = [
    ['~A','C'], ['~B','C'],
    ['~C','D'], ['~C','E'],
    ['~A','F'], ['~F','~B'],
    ['~E','G'],
    ['~G']   # negated conclusion
]

def neg(l): 
    return l[1:] if l.startswith('~') else '~' + l

def resolve(c1, c2):
    out = []
    for l1 in c1:
        for l2 in c2:
            if l1 == neg(l2):
                r = list(set(c1 + c2))
                r.remove(l1)
                r.remove(l2)
                out.append(sorted(list(set(r))))
    return out

def resolution():
    seen = set()
    while True:
        new = []
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                for r in resolve(clauses[i], clauses[j]):
                    if r == []:
                        print("Derived empty clause: KB ENTAILS G")
                        return True
                    t = tuple(r)
                    if t not in seen:
                        seen.add(t)
                        new.append(r)
        if not new:
            print("No contradiction found: KB does NOT entail G")
            return False
        clauses.extend(new)

# ----------- RUN -----------
print("Truth-table entailment:", truth_entails())
resolution()
