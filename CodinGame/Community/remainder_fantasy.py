#!/usr/bin/env python3

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a//b)*v)

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

# Solveur chinois general (cas NON p-e-e)
# (utilise la decompositon primale donc, evidemment,
#  a ne pas utiliser dans le cas plus simple des modulos
#  2-a-2 p-e-e)
# E une liste de couples (a,n) pour ? = a mod n
def solveur_chinois(Decomp,E):
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

def decomp(n):
    F = []
    m = 0
    while n%2==0:
        n //= 2
        m += 1
    if m>0:
        F.append((2,m))
    i = 3
    while n>1 and i*i<=n:
        m = 0
        while n%i==0:
            n //= i
            m += 1
        if m>0:
            F.append((i,m))
        i += 2
    if n>1:
        F.append((n,1))
    return F

def main():
    N = int(input())
    D = {}
    E = []
    for _ in range(N):
        m,r = map(int,input().split())
        E.append((r,m))
        D[m] = decomp(m)
    x,p = solveur_chinois(D,E)
    if any(x<m for _,m in E):
        x += p
    print(x)

main()
