#!/usr/bin/env python

# Chaine de Markov dont les etats sont les
# case x {0,1,2} pour les compter les doubles consecutifs
# M[i][j] = probabilite de transition de la "case" i vers la "case" j

# on negligera la regle suivante :
# si on tombe sur une case CC/CH qui nous fait retomber sur une
# telle case apres avoir tire une carte de deplacement, alors on
# devrait retirer une carte et potentiellement se redeplacer...

JAIL = 10
GO2JAIL = 30
CC = [2,17,33]
CH = [7,22,36]

def s(c,d):
    return 40*d+c

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
    M = [[0. for _ in xrange(3*40)] for _ in xrange(3*40)]
    for i in xrange(40):
        for d in xrange(3):
            for a in xrange(1,D+1):
                for b in xrange(1,D+1):
                    if a==b:
                        dj = d+1
                        if dj==3:
                            M[s(i,d)][s(JAIL,0)] += 1./(D*D)
                            continue
                    else:
                        dj = 0
                    j = (i+a+b)%40
                    if j in CC:
                        M[s(i,d)][s(0,dj)] += 1./16. * 1./(D*D)
                        M[s(i,d)][s(JAIL,dj)] += 1./16. * 1./(D*D)
                        M[s(i,d)][s(j,dj)] += 14./16. * 1./(D*D)
                        continue
                    if j in CH:
                        M[s(i,d)][s(0,dj)] += 1./16. * 1./(D*D)
                        M[s(i,d)][s(JAIL,dj)] += 1./16. * 1./(D*D)
                        M[s(i,d)][s(11,dj)] += 1./16. * 1./(D*D)
                        M[s(i,d)][s(24,dj)] += 1./16. * 1./(D*D)
                        M[s(i,d)][s(39,dj)] += 1./16. * 1./(D*D)
                        M[s(i,d)][s(5,dj)] += 1./16. * 1./(D*D)
                        M[s(i,d)][s(nextR(j),dj)] += 2./16. * 1./(D*D)
                        M[s(i,d)][s(nextU(j),dj)] += 1./16. * 1./(D*D)
                        M[s(i,d)][s((j-3)%40,dj)] += 1./16. * 1./(D*D)
                        M[s(i,d)][s(j,dj)] += 6./16. * 1./(D*D)
                        continue
                    if j==GO2JAIL:
                        j = JAIL
                    M[s(i,d)][s(j,dj)] += 1./(D*D)
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

def main():
    #M = genM(6)
    M = genM(4)
    # verif somme lignes = 1
    #for i in xrange(3*40):
    #    print i,sum(M[i][j] for j in xrange(3*40))
    # on calcule la matrice apres ~10^6 iterations :
    Minf = expo(M,1<<20)
    # les colonnes sont maintenant constantes dans la
    # conf stationnaires
    P = [(100.*sum(Minf[0][s(j,d)] for d in xrange(3)),j) for j in xrange(40)]
    P.sort(reverse=True)
    print P[:3]

main()
