#!/usr/bin/env python

import sys

# Code pour decouvrir que la fonction
# de Grundy est periodique de valeurs
# 0 0 1 1 2 2 3 3 4
def mex(succ):
    i = 0
    while i in succ:
        i += 1
    return i

G = [-1 for _ in xrange(51)]
G[0] = 0
G[1] = 0
def grundy(n):
    if G[n]>=0:
        return G[n]
    succ = set()
    for k in [2,3,5,7,11,13]:
        if k>n:
            break
        succ.add(grundy(n-k))
    g = mex(succ)
    G[n] = g
    return g

# Fonction de Grundy decouverte
G = [0,0,1,1,2,2,3,3,4]

def main():
    #for i in xrange(50):
    #    print i,grundy(i)
    #return
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        A = map(int,sys.stdin.readline().split())
        if reduce((lambda x,y: x^y),map((lambda x: G[x%len(G)]),A))==0:
            print 'Sandy'
        else:
            print 'Manasa'

main()
