#!/usr/bin/env python

# On a une chaine de Markov, dont on voudrait la distribution limite
# (verifiant MX = X). Mais elle n'est pas irreductible car les
# etats * et % sont captifs (et que le graphe n'est pas necessairement
# fortement connexe).
# On peut approximer en elevant la matrice a une puissance assez grande mais
# cela prend un peu trop de temps (certains testcases sont tres
# lents a converger).
# On se restreint aux cases libres de la composante fortement connexe de
# l'etat initial (sans les % et les *).
# On va calculer depuis chaque etat a la probabilite d'atteindre une sortie.
# Cela verifie a peu pres le meme systeme que la chaine de Markov classique
# sauf que les % et les * correspondent a des constantes (0 pour les * et
# 1 pour les %). Ne reste plus qu'a resoudre le systeme lineaire par pivot
# de Gauss.


## Pivot de Gauss (code de tryalgo)
def is_zero(x):
    return -1e-6 < x < 1e-6

GJ_ZERO_SOLUTION = 0
GJ_UNE_SOLUTION = 1
GJ_PLUSIEURS_SOLUTIONS = 2

def gauss_jordan(A, x, b):
    n = len(x)
    m = len(b)
    #assert len(A) == m and len(A[0]) == n
    S = []
    for i in xrange(m):
        S.append(A[i][:] + [b[i]])
    S.append(range(n))
    k = diagonalize(S, n, m)
    if k < m:
        for i in xrange(k, m):
            if not is_zero(S[i][n]):
                return GJ_ZERO_SOLUTION
    for j in xrange(k):
        x[S[m][j]] = S[j][n]
    if k < n:
        for j in xrange(k, n):
            x[S[m][j]] = 0
        return GJ_PLUSIEURS_SOLUTIONS
    return GJ_UNE_SOLUTION

def diagonalize(S, n, m):
    for k in xrange(min(n, m)):
        val, i, j = max((abs(S[i][j]), i, j)
                        for i in xrange(k, m) for j in xrange(k, n))
        if is_zero(val):
            return k
        S[i], S[k] = S[k], S[i]
        for r in xrange(m + 1):
            S[r][j], S[r][k] = S[r][k], S[r][j]
        pivot = float(S[k][k])
        for j in xrange(k, n + 1):
            S[k][j] /= pivot
        for i in xrange(m):
            if i != k:
                fact = S[i][k]
                for j in xrange(k, n + 1):
                    S[i][j] -= fact * S[k][j]
    return min(n, m)
##

def init_state():
    for i in xrange(n):
        for j in xrange(m):
            if G[i][j]=='A':
                G[i][j] = 'O'
                return (i,j)

# Pour le calcul de la composante fortement connexe, le pb vient des tunnels
# qui fonctionnent comme des liens orientes des voisins de la cellule
# de depart a la cellule d'arrivee, mais ils ne sont irreversibles que
# lorsque la cellule d'arrivee est "bloquee", dans ce cas on peut simplement
# remplacer la cellule de depart par une mine et oublier le tunnel.
# La composante fortement connexe devient alors une simple composante
# connexe.
def trap():
    for x in xrange(n):
        for y in xrange(m):
            if T[x+n*y]!=x+n*y:
                i,j = T[x+n*y]%n,T[x+n*y]//n
                blocked = True
                for (vi,vj) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=vi<n and 0<=vj<m and G[vi][vj]!='#':
                        blocked = False
                        break
                if blocked:
                    G[x][y] = '*'
                    T[x+n*y] = x+n*y

# dfs depuis la cellule de depart pour numeroter les sommets de
# sa composante fortement connexe
def states(i,j):
    global S
    for (vi,vj) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0<=vi<n and 0<=vj<m and G[vi][vj]=='O' and num[T[vi+n*vj]]<0:
            num[T[vi+n*vj]] = S
            S += 1
            states(T[vi+n*vj]%n,T[vi+n*vj]//n)

def main():
    global n,m,G,T,num,S
    n,m,k = map(int,raw_input().split())
    if n==m==1:
        print 0
        return
    G = [list(raw_input()) for _ in range(n)]
    T = range(n*m)
    for _ in xrange(k):
        i1,j1,i2,j2 = map((lambda x: int(x)-1),raw_input().split())
        T[i1+n*j1] = i2+n*j2
        T[i2+n*j2] = i1+n*j1
    Ai,Aj = init_state()
    num = [-1]*(n*m)
    num[Ai+n*Aj] = 0
    S = 1
    trap()
    states(Ai,Aj)
    M = [[0.]*S for _ in xrange(S)]
    for i in xrange(S):
        M[i][i] = -1.
    B = [0.]*S
    out = False
    mines = False
    for i in xrange(n):
        for j in xrange(m):
            if num[i+n*j]>=0:
                #assert(G[i][j]=='O')
                V = list(filter((lambda v: 0<=v[0]<n and 0<=v[1]<m and G[v[0]][v[1]]!='#'), [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]))
                #assert(len(V)>0)
                for (vi,vj) in V:
                    if G[vi][vj]=='*':
                        mines = True
                        continue
                    if G[vi][vj]=='%':
                        out = True
                        B[num[i+n*j]] -= 1./len(V)
                    else:
                        M[num[i+n*j]][num[T[vi+n*vj]]] = 1./len(V)
    if not out:
        print 0
    elif not mines:
        print 1
    else:
        X = [None]*S
        gauss_jordan(M,X,B)
        print X[num[Ai+n*Aj]]

main()
