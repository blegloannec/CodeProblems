import sys
from collections import defaultdict

def depth(u, u0=None):
    du = 0
    for v in T[u]:
        if v!=u0:
            du = max(du,1+depth(v,u))
    D[u] = du
    return du

def maj(u, u0=None, p0=0):
    p,p2 = p0,0
    for v in T[u]:
        if v!=u0 and 1+D[v]>=p:
            p,p2 = 1+D[v],p
    P[u] = p
    for v in T[u]:
        if v!=u0:
            maj(v,u,1+p2 if 1+D[v]==p else 1+p)

def main():
    global T,D,P
    m = int(sys.stdin.readline())
    T = defaultdict(list)
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        T[u].append(v)
        T[v].append(u)
    u0 = next(iter(T))
    D = {}
    depth(u0)
    P = {}
    maj(u0)
    print(min(P[u] for u in P))
    
main()
