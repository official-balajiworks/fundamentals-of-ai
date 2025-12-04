import random

def conflicts(s):
    n=len(s)
    return sum(s[i]==s[j] or abs(s[i]-s[j])==abs(i-j)
               for i in range(n) for j in range(i+1,n))

def hill_climb(n):
    s=[random.randrange(n) for _ in range(n)]
    while True:
        curr=conflicts(s)
        if curr==0: return s
        neigh=[]
        for c in range(n):
            for r in range(n):
                if r!=s[c]:
                    t=s[:]; t[c]=r
                    neigh.append((conflicts(t),t))
        best=min(neigh)[1]
        if conflicts(best)>=curr: return s
        s=best

print("N-Queens:", hill_climb(8))
