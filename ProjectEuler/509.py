#!/usr/bin/env python

# Code pour intuiter la fonction de Grundy
def mex(succ):
    i = 0
    while i in succ:
        i += 1
    return i

G = [-1 for _ in xrange(101)]
G[0] = 0
def grundy(n):
    if G[n]>=0:
        return G[n]
    succ = set()
    for k in xrange(1,n):
        if n%k==0:
            succ.add(grundy(n-k))
    g = mex(succ)
    G[n] = g
    return g

# Code pour verif
def L(n):
    cpt = 0
    for a in xrange(1,n):
        for b in xrange(1,n):
            for c in xrange(1,n):
                if grundy(a)^grundy(b)^grundy(c)!=0:
                    cpt += 1
    return cpt

# Fonction de Grundy decouverte :
# grundy(n) = valuation 2-adique de n
# ie plus grande puissance de 2 divisant n
# ou encore nb de trailing 0s de l'ecriture binaire

def val2(n):
    v = 0
    while n%2==0:
        n /= 2
        v += 1
    return v

def main():
    #for i in xrange(1,100):
    #    print i, grundy(i), val2(i)
    # Verif donnees du pb :
    #print L(11)
    #print L(101)
    N = 123456787654321
    VMAX = 47
    # T[i] le nb de nb <=N de valuation 2-adique exactement i
    T = [N/(1<<i) - N/(1<<(i+1)) for i in xrange(VMAX)]
    #print sum(T)
    # bourrinage en O(VMAX^3) pour compter
    # (pourrait etre fait en O(VMAX^2) en comptant
    # a la place les position perdantes, car alors
    # c=a^b, mais c'est bien assez rapide comme ca)
    cpt = 0
    for a in xrange(VMAX):
        for b in xrange(VMAX):
            for c in xrange(VMAX):
                if a^b^c!=0:
                    cpt = (cpt + T[a]*T[b]*T[c]) % 1234567890
    print cpt
    
main()
