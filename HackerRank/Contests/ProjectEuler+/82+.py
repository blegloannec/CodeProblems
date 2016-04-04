#!/usr/bin/python

import sys
from heapq import *

def pseudo_dijkstra(M):
    V = [M[i][0] for i in range(len(M))]
    for j in range(1,len(M)):
        Q = []
        visited = [False for _ in range(len(M))]
        # maj valeur en arrivant par la gauche
        for i in range(len(M)):
            V[i] += M[i][j]
            heappush(Q,(V[i],i))
        if j==len(M)-1:
            return heappop(Q)[0]
        # propagation des valeurs dans la colonne en visitant
        # les cellules de la plus petite a la plus grande
        # (facon dijkstra)
        while Q!=[]:
            v,i = heappop(Q)
            if visited[i]:
                continue
            if i>0 and not visited[i-1] and v+M[i-1][j]<V[i-1]:
                V[i-1] = v+M[i-1][j]
                heappush(Q,(V[i-1],i-1))
            if i<len(M)-1 and not visited[i+1] and v+M[i+1][j]<V[i+1]:
                V[i+1] = v+M[i+1][j]
                heappush(Q,(V[i+1],i+1))
            visited[i] = True

def main():
    N = int(sys.stdin.readline())
    M = []
    for _ in range(N):
        M.append(map(int,sys.stdin.readline().split()))
    print pseudo_dijkstra(M)

main()
