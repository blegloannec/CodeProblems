#!/usr/bin/env python3

import numpy

# chaine de Markov a 900 etats pour 1 puce
# runs in ~1.5s with python3 thanks to numpy

N,S = 30,50
N2 = N*N

def genM():
    M = [[0.]*N2 for _ in range(N2)]
    for i in range(N):
        for j in range(N):
            V = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            V = list(filter((lambda X: 0<=X[0]<N and 0<=X[1]<N),V))
            nbV = len(V)
            for (x,y) in V:
                M[i*N+j][x*N+y] = 1./nbV
    return M

def main():
    # O(N^6 log S) mais tres rapide avec numpy
    M = numpy.matrix(genM())**S
    E = 0.
    # O(N^4)
    for c in range(N2):
        # proba que la case c soit vide
        E0 = 1.
        for p in range(N2):
            # propa que la puce p ne soit pas dans la case c
            E0 *= 1. - M[p,c]
        E += E0
    print('%.6f' % E)
     
main()
