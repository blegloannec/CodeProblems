#!/usr/bin/env python3

from collections import defaultdict

# on cherche une *permutation* des cases dans laquelle
# chaque case est envoyee sur une voisine
# et il n'y a pas de cycle de taille 2

# NB : il n'y a pas de solution pour n impair
# (sur un damier, chaque case doit etre envoyee
#  de facon injective sur une case de l'autre couleur,
#  mais il n'y a pas le meme nombre de cases de chaque
#  couleur si la taille est impaire) 

# NB (a posteriori) : la solution etait directement sur l'OEIS !
# ce qui explique le difficulty rating de seulement 50%
# pour un pb aussi technique
# http://oeis.org/A216678
# http://oeis.org/A216800

N = 10

# Methode 1 : approche similaire au pb 237
# dans une configuration valide, considerons la frontiere
# entre 2 colonnes
# il y a 3 possibilites par case : une fleche vers la droite/gauche
# ou pas de franchissement

# runs in < 2s with pypy!

def encode(T):
    res = 0
    for t in T:
        res = 3*res+t
    return res

def analyse(T):
    U,D,L,R = 0,1,2,3 # Up, Down, ...
    if T[0]==U or T[N-1]==D or any(T[i]==D and T[i+1]==U for i in range(N-1)):
        return None
    P = [0]*N # counting predecessors
    for i in range(N):
        if T[i]==U:
            P[i-1] += 1
        elif T[i]==D:
            P[i+1] += 1
    I,O,A = [1]*N,[1]*N,[] # in and out frontiers
    # 0 = <--  &  2 = -->
    for i in range(N):
        if P[i]>1: # not injective
            return None
        if T[i]==L:
            I[i] = 0
            if P[i]==0: # need for an in-arrow
                O[i] = 0
        elif T[i]==R:
            O[i] = 2
            if P[i]==0: # need for an in-arrow
                I[i] = 2
        elif P[i]==0:
            # need for an in-arrow but 2 possible choices
            A.append(i) # "ambiguous" cells
    return I,O,A

# generate all possible choices from ambiguities
def choices(I,O,A,n=0):
    if n==len(A):
        yield I,O
    else:
        i = A[n]
        I[i],O[i] = 1,0  # | . <-|-
        for X in choices(I,O,A,n+1):
            yield X
        I[i],O[i] = 2,1  # -|-> . |
        for X in  choices(I,O,A,n+1):
            yield X

def gen_transitions():
    Trans = defaultdict(list)
    for n in range(4**N):
        T = [] # out arrows of a column
        for _ in range(N):
            T.append(n&3)
            n >>= 2
        X = analyse(T)
        if X==None: # non-valid configuration
            continue
        I,O,A = X
        for (i,o) in choices(I,O,A):
            Trans[encode(i)].append(encode(o))
    return Trans

Trans = gen_transitions()
I0 = encode([1]*N) # initial frontier

memo = {}
def compte(n=N,c0=I0):
    if n==0:
        return int(c0==I0)
    if (n,c0) in memo:
        return memo[n,c0]
    memo[n,c0] = sum(compte(n-1,c) for c in Trans[c0])
    return memo[n,c0]

print(compte())



# Methode 0 : enumeration brutale des cycles
#             + prog. dyn. pour la decomposition
# (fonctionne pour N<=6)
def cycle(T,C,x,y,x0,y0):
    for (vx,vy) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if 0<=vx<N and 0<=vy<N:
            if (vx,vy)==(x0,y0):
                if C>2:
                    yield C
            elif not T[N*vx+vy]:
                T[N*vx+vy] = True
                for C0 in cycle(T,C+1,vx,vy,x0,y0):
                    yield C0
                T[N*vx+vy] = False

memo = {}
def dp(T):
    K = tuple(T)
    if K in memo:
        return memo[K]
    try:
        i = T.index(False)
    except ValueError:
        return 1
    T[i] = True
    x0,y0 = i//N,i%N
    res = 0
    for _ in cycle(T,1,x0,y0,x0,y0): # T en place
        res += dp(T)
    T[i] = False # pour utiliser T en place
    memo[K] = res
    return res
        
#print(dp([False]*(N*N)))
