def unify(a, b, s):
    if s is None: return None
    if a == b: return s
    if isinstance(a,str) and a.islower(): return {**s, a:b}
    if isinstance(b,str) and b.islower(): return {**s, b:a}
    if a[0]!=b[0] or len(a)!=len(b): return None
    for x,y in zip(a[1:],b[1:]): s = unify(x,y,s)
    return s

def sub(x,s):
    if isinstance(x,str): return s.get(x,x)
    return (x[0],)+tuple(sub(a,s) for a in x[1:])

def resolve(C1,C2):
    for a in C1:
        for b in C2:
            if a[0]=="¬" and a[1]==b or b[0]=="¬" and b[1]==a:
                s = unify(a[1], b[1], {})
                if s is None: continue
                nc = {sub(x,s) for x in C1|C2}
                nc -= {sub(a,s), sub(b,s)}
                return nc
    return None

def resolution(KB):
    KB=[set(c) for c in KB]
    while True:
        new=[]
        for i in range(len(KB)):
            for j in range(i+1,len(KB)):
                r = resolve(KB[i], KB[j])
                if r is not None:
                    if not r: return True
                    new.append(frozenset(r))
        if all(n in KB for n in new): return False
        KB += new

# ---------- EXAMPLE ----------
# From:  ¬P(x) ∨ Q(x),   P(a)   prove Q(a)
KB = [
    {("¬",("P","x")), ("Q","x")},
    {("P","a")}
]

print("Entails?", resolution(KB))
