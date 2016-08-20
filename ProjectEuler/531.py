#!/usr/bin/env python

from fractions import gcd

# Si n et m sont p-e-e il y a une unique solution
# modulo nm par thm chinois.

# Sinon, si n = p1^a1...pk^ak (decomposition primale)
# et m = q1^b1...ql^bl
# alors x = A mod n <=> x = A mod pi^ai pour tout i
# et x = B mod n <=> x = B mod qi^bi pour tout i

# S'il existe i,j tels que pi = qj alors on a les
# 2 equations x = A mod pi^ai et x = B mod pi^bi.
# Supposons ai<=bi, alors pi^ai | pi^bi et
# donc x = B mod pi^bi => x = B mod pi^ai
# donc on doit avoir A mod pi^ai = B mod pi^ai
# auquel cas on peut ne garder que l'equation
# x = B mod pi^bi.

# On se ramene ainsi a un systeme d'equations
# dont les modules sont 2-a-2 p-e-e que l'on peut
# resoudre par thm chinois (solution unique modulo
# le ppcm de n et m).
# On pourrait optimiser en groupant des facteurs...


def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def rev_chinois(a,p,b,q):
    g,u,v = bezout(p,q)
    assert(g==1)
    return (b*u*p+a*v*q)%(p*q)

def G(Decomp,a,n,b,m):
    if gcd(n,m)==1:
        # cas p-e-e
        return rev_chinois(a,n,b,m)
    Dn,Dm = Decomp[n],Decomp[m]
    i,j = 0,0
    E = []
    while i<len(Dn) or j<len(Dm):
        if i<len(Dn) and j<len(Dm) and Dn[i][0]==Dm[j][0]:
            if Dn[i][1]>=Dm[j][1]:
                if (a-b)%(Dm[j][0]**Dm[j][1])!=0:
                    return 0
                f = Dn[i][0]**Dn[i][1]
                E.append((a%f,f))
            else:
                if (a-b)%(Dn[i][0]**Dn[i][1])!=0:
                    return 0
                f = Dm[j][0]**Dm[j][1]
                E.append((b%f,f))
            i += 1
            j += 1
        elif j==len(Dm) or (i<len(Dn) and Dn[i][0]<Dm[j][0]):
            f = Dn[i][0]**Dn[i][1]
            E.append((a%f,f))
            i += 1
        else:
            f = Dm[j][0]**Dm[j][1]
            E.append((b%f,f))
            j += 1
    return solve(E)

def solve(E):
    while len(E)>1:
        a,n = E.pop()
        b,m = E.pop()
        E.append((rev_chinois(a,n,b,m),n*m))
    return E[0][0]

def sieve_decomp(N):
    P = [True for _ in xrange(N)]
    Decomp = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Decomp[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k/i
                while l%i==0:
                    l /= i
                    m += 1
                Decomp[k].append((i,m))
    return P,Decomp

def eulerphi(decomp):
    res = 1
    for (p,m) in decomp:
        res *= (p-1)*p**(m-1)
    return res

def main():
    A,B = 1000000,1005000
    _,Decomp = sieve_decomp(B)
    Tot = [eulerphi(Decomp[n]) for n in xrange(B)]
    s = 0
    for n in xrange(A,B):
        for m in xrange(n+1,B):
            s += G(Decomp,Tot[n],n,Tot[m],m)
    print s

main()
