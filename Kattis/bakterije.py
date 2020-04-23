#!/usr/bin/env python3

from itertools import product

Dir = {'U':(-1,0), 'R':(0,1), 'D':(1,0), 'L':(0,-1)}

def simuloop(G, x,y, dx,dy):
    u = (x,y, dx,dy)
    t = 0
    Time = {}
    while u not in Time:
        Time[u] = t
        for _ in range(G[x][y]):
            dx,dy = dy,-dx
        if not (0<=x+dx<H and 0<=y+dy<W):
            dx,dy = -dx,-dy
        x += dx
        y += dy
        u = (x,y, dx,dy)
        t += 1
    pre = Time[u]
    per = t-pre
    return pre, per, Time

def decomp(n):
    F = []
    i = 2
    while i*i<=n:
        m = 0
        while n%i==0:
            n //= i
            m += 1
        if m>0:
            F.append((i,m))
        i += 1
    if n>1:
        F.append((n,1))
    return F

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a//b)*v)

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

# Solveur chinois general (cas NON p-e-e)
# E une liste de couples (a,n) pour ? = a mod n
def solveur_chinois(Decomp, E):
    S = {} # S[p] = (a,x) pour ? = x mod p^a
    for (x,n) in E:
        
        for (p,a) in Decomp[n]:
            if p not in S:
                S[p] = (a,x)
            else:
                b,y = S[p]
                if (x-y)%(p**min(a,b))!=0: # pas de solution
                    return None
                if b<a:
                    S[p] = (a,x)
    x,p = 0,1
    for q in S:
        b,y = S[q]
        qb = q**b
        x,p = rev_chinois(x,p,y,qb),p*qb
    return (x,p)

def main():
    global H,W
    H,W,K = map(int,input().split())
    Xf,Yf = (int(i)-1 for i in input().split())
    Decomp = {}
    AllEq = []
    for _ in range(K):
        Xi,Yi,Ci = input().split()
        Xi, Yi = int(Xi)-1, int(Yi)-1
        Gi = [[int(c)%4 for c in input().strip()] for _ in range(H)]
        DXi, DYi = Dir[Ci]
        pre, per, Time = simuloop(Gi, Xi,Yi, DXi,DYi)
        Tf = [t for (x,y,_,_),t in Time.items() if (x,y)==(Xf,Yf)]
        AllEq.append([(t,per) if t>=pre else (t,0) for t in Tf])
        Decomp[per] = decomp(per)
    tmin = INF = float('inf')
    for E in product(*AllEq):
        Fixed = [t for t,per in E if per==0]
        if Fixed:
            tfix = Fixed[0]
            if all(t==tfix if per==0 else tfix>=t and (tfix-t)%per==0 for t,per in E):
                tmin = min(tmin, tfix)
        else:
            tq = solveur_chinois(Decomp, E)
            if tq is not None:
                t,q = tq
                tmax = max(t for t,_ in E)
                if t<tmax:
                    t += ((tmax-t + q-1)//q)*q
                tmin = min(tmin, t)
    print(tmin if tmin<INF else -1)

main()
