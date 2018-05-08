#!/usr/bin/env python3

def test(G):
    r,c = len(G),len(G[0])
    R = [sum(L) for L in G]
    C = [sum(G[i][j] for i in range(r)) for j in range(c)]
    O = [['N']*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if (G[i][j]>0) != (R[i]>0 and C[j]>0):
                return None
            if G[i][j]:
                O[i][j] = 'P' if R[i]==1 or C[j]==1 else 'I'
    return O

def main():
    T = int(input())
    for _ in range(T):
        r,c = map(int,input().split())
        G = [list(map(int,input())) for _ in range(r)]
        O = test(G)
        if O==None:
            print('impossible')
        else:
            for L in O:
                print(''.join(L))
        print('----------')

main()
