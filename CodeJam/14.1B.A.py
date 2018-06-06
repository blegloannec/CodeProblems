#!/usr/bin/env python

import sys

# sgn(aaa,bb,c,aa) = (abca, [3,2,1,2])
def sgn(w):
    Chr = [w[0]]
    Cpt = [1]
    for i in xrange(1,len(w)):
        if w[i]==Chr[-1]:
            Cpt[-1] += 1
        else:
            Chr.append(w[i])
            Cpt.append(1)
    return Chr,Cpt

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N = int(sys.stdin.readline())
        Sgn = [] # signatures des inputs
        for n in xrange(N):
            Sgn.append(sgn(sys.stdin.readline().strip()))
        possible = True
        LCpt = [[Sgn[0][1][j]] for j in xrange(len(Sgn[0][1]))]
        for i in xrange(1,N):
            if Sgn[i][0]!=Sgn[0][0]: # verif memes blocs partout
                possible = False
                break
            for j in xrange(len(LCpt)): # listes de tailles des blocs
                LCpt[j].append(Sgn[i][1][j])
        if not possible:
            print 'Case #%d: Fegla Won' % (t)
            continue
        res = 0
        # pour chaque bloc, le nb minimal d'operations est la somme des
        # ecarts a la mediane des tailles du bloc
        for j in xrange(len(LCpt)):
            LCpt[j].sort() # pour mediane en O(n log n), suffisant ici
            med = LCpt[j][N/2] # mediane
            for i in xrange(N):
                res += abs(Sgn[i][1][j]-med)
        print 'Case #%d: %d' % (t,res)

main()
