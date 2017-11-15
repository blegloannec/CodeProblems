#!/usr/bin/env python

# runs in 11s with pypy

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]

def val(n,p):  # p-valuation de n
    m = 0
    while n%p==0:
        m += 1
        n /= p
    return m

def fact_val(n,p):  # p-valuation de n!
    cpt = 0
    q = p
    while q<=n:
        cpt += n/q
        q *= p
    return cpt

# produits <=R de facteurs Pi^d avec d<=Di
def target(D,R,full=False):
    S = [1]
    for ip in xrange(len(P)):
        for i in xrange(len(S)):
            q = S[i]
            for _ in xrange(D[ip]):
                q *= P[ip]
                if q>R:
                    break
                S.append(q)
    if full:
        S.sort(reverse=True)
        return S
    else:
        return max(S)

def main():
    N = 43
    F = 1
    for i in xrange(2,N+1):
        F *= i
    R = int(F**(1./3))
    D = [fact_val(N,p) for p in P]
    ma,mc = 1,float('inf')
    Sa = target(D,R,True)
    # on essaye les 15 (suffisant ici) a les plus proches
    # de la racine cubique de F
    for a in Sa[:15]:
        bc = F/a
        Rbc = int(bc**(1./2))
        Dbc = [D[i]-val(a,P[i]) for i in xrange(len(P))]
        # b le plus proche de la racine carree de bc
        b = target(Dbc,Rbc)
        if a<b:
            c = bc/b
            if c*ma<mc*a:
                ma,mb,mc = a,b,c
    print ma+mb+mc

main()
