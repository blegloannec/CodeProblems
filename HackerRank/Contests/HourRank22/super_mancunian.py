#!/usr/bin/env python3

# find version iterative car python...
def find(x):
    L = []
    while T[x]>=0:
        L.append(x)
        x = T[x]
    for l in L:
        T[l] = x
    return x

def union(x,y):
    T[find(y)] = find(x)

def main():
    global T
    n,m = map(int,input().split())
    E = []
    for _ in range(m):
        a,b,w = map(int,input().split())
        if a!=b:
            E.append((w,a-1,b-1))
    T = [-1]*n
    E.sort()
    # Kruskal std
    s = 0
    for (w,a,b) in E:
        if find(a)!=find(b):
            union(a,b)
            s += w
            wmax = w
    # Kruskal passe 2
    T = [-1]*n
    nb = 0
    for (w,a,b) in E:
        if find(a)!=find(b):
            if w<wmax:
                union(a,b)
            else:
                nb += 1
    print(s-wmax,nb)

main()
