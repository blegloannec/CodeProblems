#!/usr/bin/env python

from collections import deque

# rather boring BFS, not really optimized
# better should have done this one in C++ by the way

# une configuration sera representee par un tuple
# (etage ascenseur,[positions puces],[positions generateurs])
# ou les listes sont codees dans un entier en base 4

def floor(C,n):
    return (C>>(2*n))&3

def ufloor(n):
    return 1<<(2*n)


# Example
N = 2
start = (0,int('00',4),int('12',4))
dest = (3,int('33',4),int('33',4))

# Part One, <2s with pypy
N = 5
start = (0,int('00211',4),int('00111',4))
dest = (3,int('33333',4),int('33333',4))

# Part Two, ~50s with pypy
N = 7
start = (0,int('0021100',4),int('0011100',4))
dest = (3,int('3333333',4),int('3333333',4))


# codage d'un triplet en un seul int pour economiser la memoire
def encode(E,C,G):
    return E|(C<<2)|(G<<(2*N+2))

start = encode(*start)
dest = encode(*dest)

mask = (1<<(2*N))-1
def decode(X):
    return (X&3,(X>>2)&mask,X>>(2*N+2))


# verifie que le floor f est valide
def valid_floor(f,C,G):
    return not (any(floor(G,i)==f for i in xrange(N)) and any(floor(C,i)==f and not floor(G,i)==f for i in xrange(N)))

# genere les configurations suivantes valides
def next_conf(X):
    E,C,G = decode(X)
    # puces a l'etage
    CE = [i for i in xrange(N) if floor(C,i)==E]
    # generateurs a l'etage
    GE = [i for i in xrange(N) if floor(G,i)==E]
    # deplacement
    for f in [-1,1]:
        F = E+f
        if 0<=F<=3:
            # 1 puce
            for i in xrange(len(CE)):
                C += f*ufloor(CE[i])
                if valid_floor(F,C,G) and valid_floor(E,C,G):
                    yield encode(F,C,G)
                    # 2 puces (si on peut envoyer la 1ere)
                    for j in xrange(i+1,len(CE)):
                        C += f*ufloor(CE[j])
                        if valid_floor(F,C,G) and valid_floor(E,C,G):
                            yield encode(F,C,G)
                        C -= f*ufloor(CE[j])
                C -= f*ufloor(CE[i])
            # 1 generateur
            for i in xrange(len(GE)):
                G += f*ufloor(GE[i])
                if valid_floor(F,C,G) and valid_floor(E,C,G):
                    yield encode(F,C,G)
                # 1 generateur et sa puce
                if floor(C,GE[i])==E:
                    C += f*ufloor(GE[i])
                    if valid_floor(F,C,G) and valid_floor(E,C,G):
                        yield encode(F,C,G)
                    C -= f*ufloor(GE[i])
                # 2 generateurs
                for j in xrange(i+1,len(GE)):
                    G += f*ufloor(GE[j])
                    if valid_floor(F,C,G) and valid_floor(E,C,G):
                        yield encode(F,C,G)
                    G -= f*ufloor(GE[j])
                G -= f*ufloor(GE[i])

# simple BFS dans le graphe des confs
def bfs(start,dest):
    Q = deque([start])
    dist = {start:0}
    while Q:
        u = Q.popleft()
        d = dist[u]
        for v in next_conf(u):
            if v==dest:
                return d+1
            if v not in dist:
                dist[v] = d+1
                Q.append(v)

print bfs(start,dest)
