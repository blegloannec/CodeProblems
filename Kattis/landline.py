#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def find(T, x):
    if T[x] is None:
        return x
    T[x] = find(T, T[x])
    return T[x]

def union(T, x, y):
    x0 = find(T, x)
    y0 = find(T, y)
    if x0==y0:
        return False
    T[y0] = x0
    return True

INF = float('inf')

def kruskal(N, C, E):
    E.sort()
    T = [None]*N
    MST = 0
    for l,x,y in E:
        if union(T, x, y):
            MST += l
            C -= 1
            if C==1:
                break
    return MST if C==1 else INF

def main():
    N,M,P = map(int, input().split())
    if P==N:  # particular case: all insecure
        if M==N*(N-1)//2:  # clique
            input()
            print(sum(int(input().split()[2]) for _ in range(M)))
        else:
            print('impossible')
        return
    InsecV = [int(x)-1 for x in input().split()]
    Insec = [False]*N
    for x in InsecV:
        Insec[x] = True
    E = []
    InsecE = [INF for _ in range(N)]
    for _ in range(M):
        x,y,l = map(int, input().split())
        x -= 1
        y -= 1
        if Insec[x] or Insec[y]:
            if not Insec[y] and l<InsecE[x]:
                InsecE[x] = l
            elif not Insec[x] and l<InsecE[y]:
                InsecE[y] = l
        else:
            E.append((l,x,y))
    res = sum(InsecE[x] for x in InsecV)
    if res<INF:
        res += kruskal(N, N-P, E)
    print(res if res<INF else 'impossible')

main()
