#!/usr/bin/env python

import sys

# Chaine de Markov dont les etats sont les cases
# M[i][j] = probabilite de transition de la case i vers la case j

# attention ici a la regle suivante :
# CH3 + go back 3 squares -> CC3
# et on retire donc une carte

JAIL = 10
GO2JAIL = 30
CC = [2,17,33]
CH = [7,22,36]

def nextR(i):
    j = 5*(i/5+1)
    if j%10==0:
        j += 5
    return j%40

def nextU(i):
    if i<12 or i>=28:
        return 12
    return 28

def genM(D):
    M = [[0. for _ in xrange(40)] for _ in xrange(40)]
    for i in xrange(40):
        for a in xrange(1,D+1):
            for b in xrange(1,D+1):
                j = (i+a+b)%40
                if j in CC:
                    M[i][0] += 1./16. * 1./(D*D)
                    M[i][JAIL] += 1./16. * 1./(D*D)
                    M[i][j] += 14./16. * 1./(D*D)
                    continue
                if j in CH:
                    M[i][0] += 1./16. * 1./(D*D)
                    M[i][JAIL] += 1./16. * 1./(D*D)
                    M[i][11] += 1./16. * 1./(D*D)
                    M[i][24] += 1./16. * 1./(D*D)
                    M[i][39] += 1./16. * 1./(D*D)
                    M[i][5] += 1./16. * 1./(D*D)
                    M[i][nextR(j)] += 2./16. * 1./(D*D)
                    M[i][nextU(j)] += 1./16. * 1./(D*D)
                    if j==36: # CH3 -> CC3
                        M[i][33] += 1./16. * 1./(D*D) * 14./16.
                        M[i][0] += 1./16. * 1./(D*D) * 1./16.
                        M[i][JAIL] += 1./16. * 1./(D*D) * 1./16.
                    else:
                        M[i][(j-3)%40] += 1./16. * 1./(D*D)
                    M[i][j] += 6./16. * 1./(D*D)
                    continue
                if j==GO2JAIL:
                    j = JAIL
                M[i][j] += 1./(D*D)
    return M

def matmult(A,B):
    pB = zip(*B)
    return [[sum(ea*eb for ea,eb in zip(a,b)) for b in pB] for a in A]

def expo(A,b):
    result = [[int(i==j) for j in xrange(len(A))] for i in xrange(len(A))]
    while b:
        if b & 1:
            result = matmult(result,A)
        A = matmult(A,A)
        b >>= 1
    return result

Name = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL','C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']

def main():
    N,K = map(int,sys.stdin.readline().split())
    M = genM(N)
    Minf = expo(M,1<<30)
    # les colonnes sont maintenant constantes dans la
    # conf stationnaires
    P = [(Minf[0][j],j) for j in xrange(40)]
    P.sort(reverse=True)
    print ' '.join(map((lambda x: Name[x[1]]), P[:K]))

main()
