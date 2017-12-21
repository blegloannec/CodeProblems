#!/usr/bin/env python3

import sys

# symetries (groupe D8)
def vsym(P):
    return tuple(reversed(P))

def hsym(P):
    return tuple(l[::-1] for l in P)

def dsym(P):
    return tuple(''.join(P[i][j] for i in range(len(P))) for j in range(len(P)))

def Sym(P):
    for L in [P,dsym(P)]:
        yield from [L,hsym(L),vsym(L),hsym(vsym(L))]

# lecture des regles
def parse_rules():
    Rules = {}
    for L in sys.stdin.readlines():
        L = L.strip().split(' => ')
        L,R = tuple(L[0].split('/')),tuple(L[1].split('/'))
        for P in Sym(L):
            if P in Rules:
                assert(Rules[P]==R)  # checking consistency
            else:
                Rules[P] = R
    return Rules

Rules = parse_rules()

# substitution
def step(P):
    b = 2 if len(P)%2==0 else 3
    K = len(P)//b
    Q = [[] for _ in range(K*(b+1))]
    for i in range(K):
        for j in range(K):
            p = tuple(P[i*b+k][j*b:(j+1)*b] for k in range(b))
            q = Rules[p]
            for k in range(b+1):
                Q[i*(b+1)+k].append(q[k])
    Q = [''.join(L) for L in Q]
    return Q

def sub(P,n):
    for _ in range(n):
        P = step(P)
    return P

P0 = ('.#.',
      '..#',
      '###')


# Part 1
P = sub(P0,5)
print(sum(L.count('#') for L in P))


# Part 2
# la simulation naive ici prend <3s, mais on peut faire beaucoup mieux
# un bloc de taille 3 evolue en 2*2, puis 2*3 redecoupes en 3*2, puis 3*3
# les 9 blocs de 3 evoluent alors independamment, en 3 etapes on a donc
# retrouve une substitution "classique" (hors contexte)

def rep(b):  # representative of a bloc
    return min(Sym(b))

def build_sub3():
    T = {}  # bloc   -> indice (type de blocs)
    B = []  # indice -> bloc
    for b in Rules:
        if len(b)==3:
            r = rep(b)
            if r not in T:
                T[r] = len(B)
                B.append(r)
    S = [[] for _ in range(len(B))]
    for b in range(len(B)):
        P = sub(B[b],3)
        for i in range(3):
            for j in range(3):
                p = rep(tuple(P[i*3+k][j*3:(j+1)*3] for k in range(3)))
                S[b].append(T[p])
    return B,T,S

B,T,S = build_sub3()

# comme n est petit on fait une simple prog. dyn. ici, mais si n etait enorme,
# on utiliserait une exponentiation de matrice en O(T^3 log(n)) pour T le nb
# de regles (~100)
memo = {(b,0):sum(l.count('#') for l in B[b]) for b in range(len(B))}
def cpt(b,n):
    if (b,n) in memo:
        return memo[b,n]
    memo[b,n] = sum(cpt(c,n-1) for c in S[b])
    return memo[b,n]

print(cpt(T[rep(P0)],18//3))
