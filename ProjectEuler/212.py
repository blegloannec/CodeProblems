#!/usr/bin/env python

from bisect import *

# on procede par balayage selon l'axe Z
# on a 50000 cuboides, l'espace est 10400^3
# la taille moyenne d'un cuboide est 200^3
# pour un z fixe, on a en moyenne 50000*200/10400 ~ 1000 cuboides dans le plan
# a chaque instant, on va maintenir le plan de coupe selon Z
# dans une table suivant une square-root decomposition
# sqrt(1000) ~ 32 et 10400/32 ~ 300 de l'ordre de la taille moyenne
# on aura une table 32x32 ou chaque case (i,j) contient la liste des cuboides
# qui intersectent la zone [i*10400/32,(i+1)*10400/32]x[j*10400/32,(j+1)*10400/32]
# dans le plan Z=cst courant
# a chaque evenement selon Z (debut/fin d'un cuboide) on ne recalculera que l'aire
# couverte des regions intersectees (il y en a au plus 4)
# on utilisera pour cela un algo de balayage 2D en O(n^2), mais le nb de cuboides
# par region etant en moyenne <=2 (du fait du decoupage choisi et de l'homogeneite
# de la repartition pseudo-aleatoire dans l'espace), le calcul de chaque evenement
# est en O(1), d'ou un algo en moyenne en O(n)

# runs in 2s with pypy


# union 2d en O(n^2) par balayage
# R une liste de (x,y,dx,dy)
def union_2d(R):
    X,Y = set(),[]
    for i in xrange(len(R)):
        x,y,dx,dy = R[i]
        X.add(x)
        X.add(x+dx)
        Y.append((y,True,i))
        Y.append((y+dy,False,i))
    X = sorted(list(X)) # intervalles
    Y.sort() # evenements
    # C[i] = nb de rectangles couvrant [X[i],X[i+1]]
    C = [0 for _ in xrange(len(X))]
    A,L = 0,0
    for j in xrange(len(Y)):
        if j>0:
            A += L*(Y[j][0]-Y[j-1][0])
        y,nouv,r = Y[j]
        x0,_,dx,_ = R[r]
        x1 = x0+dx
        i = bisect_left(X,x0)
        while X[i]!=x1:
            if nouv:
                C[i] += 1
                if C[i]==1:
                    L += X[i+1]-X[i]
            else:
                C[i] -= 1
                if C[i]==0:
                    L -= X[i+1]-X[i]
            i += 1
    return A


# suite pseudo-aleatoire
def gen(n):
    S = [(100003-200003*k+300007*k**3)%1000000 for k in xrange(1,56)]
    for i in xrange(6*n):
        S.append((S[-24]+S[-55])%1000000)
    C = []
    for i in xrange(n):
        C.append((S[6*i]%10000,S[6*i+1]%10000,S[6*i+2]%10000,1+(S[6*i+3]%399),1+(S[6*i+4]%399),1+(S[6*i+5]%399)))
    return C

# tri des cuboides selon Z (evenements du balayage)
def sortZ():
    Z = []
    for i in xrange(N):
        Z.append((C[i][2],True,i))
        Z.append((C[i][2]+C[i][5],False,i))
    Z.sort()
    return Z

N = 50000
#N = 100
C = gen(N)
Z = sortZ()

# balayage "naif" en O(n^3) (en pratique ~ 50000 * 1000^2 ici)
def main_n3():
    A,V = 0,0
    S = set()
    for k in xrange(len(Z)):
        if k>0:
            V += A*(Z[k][0]-Z[k-1][0])
        z,nouv,r = Z[k]
        if nouv:
            S.add(r)
        else:
            S.remove(r)
        R = [(C[r][0],C[r][1],C[r][3],C[r][4]) for r in S]
        A = union_2d(R)
    print V

# balayage + square-root decomposition (efficace ~O(n))
def main():
    K = 32
    DS = 10400/K+1
    G = [[set() for _ in xrange(K)] for _ in xrange(K)]
    GA = [[0 for _ in xrange(K)] for _ in xrange(K)]
    A,V = 0,0
    for k in xrange(len(Z)):
        if k>0:
            V += A*(Z[k][0]-Z[k-1][0])
        z,nouv,r = Z[k]
        x0,y0,_,dx,dy,_ = C[r]
        x1,y1 = x0+dx,y0+dy
        for i in xrange(x0/DS,x1/DS+1):
            for j in xrange(y0/DS,y1/DS+1):
                if nouv:
                    G[i][j].add(r)
                else:
                    G[i][j].remove(r)
                R = []
                for l in G[i][j]:
                    gx,gy = max(i*DS,C[l][0]),max(j*DS,C[l][1])
                    gdx = min((i+1)*DS,C[l][0]+C[l][3])-gx
                    gdy = min((j+1)*DS,C[l][1]+C[l][4])-gy
                    R.append((gx,gy,gdx,gdy))
                A -= GA[i][j]
                GA[i][j] = union_2d(R)
                A += GA[i][j]
    print V

main()
