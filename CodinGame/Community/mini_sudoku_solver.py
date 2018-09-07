#!/usr/bin/env python3

from itertools import permutations

n = 2
N = n*n

def precomp():
    global Avail,Pos,Used
    Avail = [set(range(1,N+1)) for _ in range(N)]
    Pos = [[] for _ in range(N)]
    Used = [0]*N
    for i in range(N):
        for j in range(N):
            if G[i][j]==0:
                Pos[i].append(j)
            else:
                Avail[i].remove(G[i][j])
                Used[j] |= 1<<G[i][j]

def backtrack(i=0):
    if i>0 and i%n==0:
        for j in range(0,N,n):
            if len(set(G[x][y] for x in range(i-n,i) for y in range(j,j+n)))<N:
                return False
    if i==N:
        return True
    # on traite la ligne i
    for P in permutations(Avail[i]):
        # conditions de carre latin
        if all(Used[Pos[i][j]]&(1<<P[j])==0 for j in range(len(Pos[i]))):
            for j in range(len(Pos[i])):
                G[i][Pos[i][j]] = P[j]
                Used[Pos[i][j]] ^= 1<<P[j]
            if backtrack(i+1):
                return True
            for j in range(len(Pos[i])):
                Used[Pos[i][j]] ^= 1<<P[j]
    return False

def main():
    global G
    G = [list(map(int,list(input()))) for _ in range(N)]
    precomp()
    assert(backtrack())
    for L in G:
        print(''.join(map(str,L)))

main()
