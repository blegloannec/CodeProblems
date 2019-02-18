#!/usr/bin/env python3

N = int(input())
X = int(input())
G = [input() for _ in range(N)]

def Idx(i,j):
    return N*j + (i if j&1 else N-1-i)

def Pos(I):
    j,i = divmod(I,N)
    return (i if j&1 else N-1-i),j

print('\n'.join(''.join(G[k][l] for k,l in (Pos((Idx(i,j)-X)%(N*N)) for j in range(N))) for i in range(N)))
