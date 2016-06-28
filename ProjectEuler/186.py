#!/usr/bin/env python3

N = 10**6
T = [-1 for _ in range(N)]
S = [1 for _ in range(N)]
PM = 524287

def find(x):
    if T[x]<0:
        return x
    x0 = find(T[x])
    T[x] = x0
    return x0

def union(x,y):
    x0,y0 = find(x),find(y)
    T[y0] = x0
    S[x0] += S[y0]

# generateur de paires
def gen():
    n = 0
    s = [(100003-200003*k+300007*k*k*k)%N for k in range(1,56)]
    # pour taille paire :
    s.append((s[-24]+s[-55])%N)
    for i in range(0,56,2):
        yield (s[i],s[i+1])
    curr = 0
    while True:
        s[curr] = (s[curr-24]+s[curr-55])%N
        curr = (curr+1)%56
        s[curr] = (s[curr-24]+s[curr-55])%N
        yield (s[curr-1],s[curr])
        curr = (curr+1)%56

def main():
    cpt = 0
    for (x,y) in gen():
        if x!=y:
            cpt += 1
            if find(x)!=find(y):
                union(x,y)
                if S[find(PM)]>=99*N/100:
                    print(cpt)
                    return

main()
