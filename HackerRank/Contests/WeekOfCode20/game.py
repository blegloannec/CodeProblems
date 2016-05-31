#!/usr/bin/env python

import sys

##
## Code trop lent, difficile de faire mieux en python
##

# N le nb total de jetons
#
# Pour K=2, chaque mouvement augmente le nb de tas d'exactement 1
# une position a M tas est perdante ssi M%2 != N%2
#
# Le jeu est la somme de ses tas, il s'analyse donc via une fonction
# de Grundy qui est le xor des fonctions de Grundy de ses tas
#
# Pour K=2, g(n)=(n+1)%2
# Pour la variante du jeu ou K>=3 est FORCE (ie on doit diviser un tas en exactement
# K tas), g(n) = (n-1)/(K-1), mais ce n'est pas utile ici
# Pour K=3, g(n)=???, doit etre calculee, mais ce serait trop lent donc on precalcule
# tout en local et on stocke les resultats
# pour K>=4, g(n)=n-1


## Analyse generale du jeu
def partitions(n,k):
    if k==1:
        yield [n]
    elif k<=n:
        for p in partitions(n-1,k-1):
            p.append(1)
            yield p
        for p in partitions(n-k,k):
            for i in xrange(k):
                p[i] += 1
            yield p

def mex(succ):
    i = 0
    while i in succ:
        i += 1
    return i
            
win = {() : 0}
def progdyn(S):
    T = tuple(S)
    if T in win:
        return win[T]
    L = len(S)
    succ = set()
    for i in xrange(L):
        for k in xrange(2,K+1):
            for p in partitions(S[i],k):
                C = S[:i]+S[i+1:]+p
                while C!=[] and C[-1]==1:
                    C.pop()
                C.sort(reverse=True)
                succ.add(progdyn(C))
    g = mex(succ)
    win[T] = g
    return g


## Progdyn pour Grundy
G = []
def grundy(n):
    if G[n]>=0:
        return G[n]
    succ = set()
    for k in xrange(2,K+1):
        for p in partitions(n,k):
            v = 0
            for x in p:
                v ^= grundy(x)
            succ.add(v)
    g = mex(succ)
    G[n] = g
    return g

def precompG():
    global G
    G = [-1 for _ in xrange(N+1)]
    G[1] = 0
    for n in xrange(1,N+1):
        print n,grundy(n)


# progdyn en O(N^2*M*X), ou X est la puissance de 2 superieure a N, pour compter les solutions
# P(n,m,x) = nb de partitions de n en m blocs dont le xor des grundy vaut x
# P(n,m,x) = sum( P(n-k,m-1,x^g(k)), k=1..n )
# NB : on peut se passer de la dimension en M (echanger les boucles sur n et m et parcourir
# les n dans l'ordre inverse), mais ca ne fait pas gagner de temps
def precompP():
    P = [[[0 for _ in xrange(X)] for _ in xrange(M+1)] for _ in xrange(N+1)]
    P[0][0][0] = 1
    for n in xrange(1,N+1):
        for m in xrange(1,M+1):
            for x in xrange(X):
                for k in xrange(1,n+1):
                    P[n][m][x] = (P[n][m][x]+P[n-k][m-1][x^G[k]])%Pr
    return P


def main():
    global Pr,G,N,M,K,X
    Pr = 1000000007
    N,M,K = map(int,sys.stdin.readline().split())
    X = 2
    while N>=X:
        X *= 2
    if K==2:
        G = [(n+1)%2 for n in xrange(N+1)]
    elif K==3:
        #precompG()  # Too slow
        G = [0,0,1,2,3,1,4,3,2,4,5,6,7,8,9,7,6,9,8,11,10,12,13,10,11,13,12,15,14,16,17,5,15,17,16,19,18,20,21,18,19,21,20,23,22,25,24,22,23,24,25,26,27,29,28,27,26,28,29,30,31,14,32,31,30,32,33,34,35,37,36,35,34,36,37,38,39,40,41,39,38,41,40,43,42,44,45,42,43,45,44,47,46,48,49,46,47,49,48,51,50,52,53,50,51,53,52,55,54,57,56,54,55,56,57,58,59,61,60,59,58,60,61,62,63,64,65,63,62,65,64,67,66,68,69,66,67,69,68,71,70,73,72,70,71,72,73,74,75,77,76,75,74,76,77,78,79,81,80,79,78,80,81,82,83,85,84,83,82,84,85,86,87,88,89,87,86,89,88,91,90,92,93,90,91,93,92,95,94,96,97,94,95,97,96,99,98,100,101,33,99,101,100,103,102,105,104,102,103,104,105,106,107,109,108,107,106,108,109,110,111,113,112,111,110,112,113,114,115,117,116,115,114,116,117,118,119,120,121,119,118,121,120,123,122,124,125,122,123,125,124,127,126,128,129,126,127,129,128,131,130,132,133,130,131,133,132,135,134,137,136,134,135,136,137,138,139,141,140,139,138,140,141,142,143,145,144,143,142,144,145,146,147,149,148,147,146,148,149,150,151,152,153,151,150,153,152,155,154,156,157,154,155,157,156,159,158,160,161,158,159,161,160,163,162,164,165,162,163,165,164,167,166,169,168,166,167,168,169,170,171,98,172,171,170,172,173,174,175,177,176,175,174,176,177,178,179,181,180,179,178,180,181,182,183,184,185,183,182,185,184,187,186,188,189,186,187,189,188,191,190,193,192,190,191,192,193,194,195,197,196,195,194,196,197,198,199,200,201,199,198,201,200,203,202,204,205,202,203,205,204,207,206,208,209,206,207,209,208,211,210,212,213,210,211,213,212,215,214,217,216,214,215,216,217,218,219,221,220,219,218,220,221,222,223,225,224,223,222,224,225,226,227,229,228,227,226,228,229,230,231,232,233,231,230,233,232,235,234,236,237,234,235,237,236,239,238,240,241,238,239,241,240,243,242,244,245,242,243,245,244,247,246,249,248,246,247,248,249,250,251,253,252,251,250,252,253,254,255,256,257,173,254,257,256,259,258,260,261,258,259,261,260,263,262,265,264,262,263,264,265,266,267,269,268,267,266,268,269,270,271,273,272,271,270,272,273,274,275,277,276,275,274,276,277,278,279,280,281,279,278,281,280,283,282,284,285,282,283,285,284,287,286,288,289,286,287,289,288,291,290,292,293,290,291,293,292,295,294,297,296,294,295,296,297,298,299,301,300,299,298]
    else:
        G = [n-1 for n in xrange(N+1)]
    P = precompP()
    cpt = 0
    for x in xrange(1,X):
        cpt = (cpt+P[N][M][x])%Pr
    print cpt

main()
