#!/usr/bin/env python

# Code pour intuiter la fonction de Grundy
def mex(succ):
    i = 0
    while i in succ:
        i += 1
    return i

G = [-1 for _ in xrange(1001)]
G[0] = 0
G[1] = 0
def grundy(n):
    if G[n]>=0:
        return G[n]
    succ = set()
    for k in xrange((n-2)/2+1):
        if n-2-k>=0:
            succ.add(grundy(k)^grundy(n-2-k))
    g = mex(succ)
    G[n] = g
    return g

# Fonction de Grundy decouverte :
# https://oeis.org/A002187
# "Has period 34 with the only exceptions at n=0, 14, 16, 17, 31, 34 and 51."
# https://oeis.org/A215721

def main():
    #for i in xrange(1,101):
    #    print "%d," % grundy(i),
    cpt = 0
    for i in xrange(1,52):
        if grundy(i)>0:
            cpt += 1
    for i in xrange(52,1000001):
        if grundy((i-1)%34+1+68)>0:
            cpt += 1
    print cpt
    
main()
