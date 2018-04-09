#!/usr/bin/env python3

from fractions import gcd

def sieve_list(N):
    P = [True]*N
    L = []
    for i in range(2,N):
        if P[i]:
            L.append(i)
            for k in range(2*i,N,i):
                P[k] = False
    return L

P = sieve_list(32000)

def decomp(n):
    F = []
    i = 0
    while n>1 and P[i]*P[i]<=n:
        m = 0
        while n%P[i]==0:
            n //= P[i]
            m += 1
        if m>0:
            F.append((P[i],m))
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

def main():
    T = int(input())
    for _ in range(T):
        a,n,b,m = map(int,input().split())
        D = {n:decomp(n),m:decomp(m)}
        E = [(a,n),(b,m)]
        res = solveur_chinois(D,E)
        if res==None:
            print('no solution')
        else:
            print(*res)

main()
