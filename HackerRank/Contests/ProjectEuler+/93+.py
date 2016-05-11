#!/usr/bin/env python

import sys
from fractions import *

# sous-ensembles de 0..n-1 de cardinal card
def subsets(n,c):
    if c==0:
        yield 0
    else:
        for x in xrange(c-1,n):
            for S in subsets(x,c-1):
                yield S | (1<<x)

def bon_compte(X,cible):
    # NB: les dictionnaires pour chaque sous-ensemble
    # peuvent etre remplaces par des listes de couples (val,expr)
    E = [{} for _ in xrange(1<<len(X))]
    for x in xrange(len(X)):
        E[1<<x][X[x]] = str(X[x])
    for c in xrange(2,len(X)+1):
        for S in subsets(len(X),c):
            for L in xrange(1,S):
                if L&S==L:
                    R = S^L
                    for vL in E[L]:
                        for vR in E[R]:
                            eL,eR = E[L][vL],E[R][vR]
                            E[S][vL] = eL # on utilise que la partie gauche
                            E[S][vL+vR] = '(%s+%s)' % (eL,eR)
                            E[S][vL-vR] = '(%s-%s)' % (eL,eR)
                            E[S][vL*vR] = '(%s*%s)' % (eL,eR)
                            if vR!=0 and vL%vR==0:
                                E[S][vL/vR] = '(%s/%s)' % (eL,eR)
    # recherche de la solution la plus proche
    # en exploitant les dictionnaires
    for d in xrange(cible+1):
        for sgn in [-1,1]:
            v = cible+sgn*d
            if v in E[-1]:
                return '%s=%d' % (E[-1][v],v)
    pass

# version modifiee pour utiliser obligatoirement tous les nbs
# et fractions autorisees (nettement plus lent en consequence)
def compte_total(X):
    E = [set() for _ in xrange(1<<len(X))]
    for x in xrange(len(X)):
        E[1<<x].add(Fraction(X[x]))
    for c in xrange(2,len(X)+1):
        for S in subsets(len(X),c):
            for L in xrange(1,S):
                if L&S==L:
                    R = S^L
                    for vL in E[L]:
                        for vR in E[R]:
                            E[S].add(vL+vR)
                            E[S].add(vL-vR)
                            E[S].add(vL*vR)
                            if vR!=0:
                                E[S].add(Fraction(vL,vR))
    return E

def main():
    m = int(sys.stdin.readline())
    X = map(int,sys.stdin.readline().split())
    E = compte_total(X)
    i = 1
    while Fraction(i) in E[-1]:
        i += 1
    i -= 1
    print i

main()
