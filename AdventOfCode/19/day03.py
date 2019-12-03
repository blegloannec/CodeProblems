#!/usr/bin/env python3

Dir = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

def cells_time(P):
    T = {}
    i = j = t = 0
    for D in P:
        di,dj = Dir[D[0]]
        s = int(D[1:])
        for _ in range(s):
            i += di
            j += dj
            t += 1
            if (i,j) not in T:
                T[i,j] = t
    return T

P1 = input().split(',')
P2 = input().split(',')
T1 = cells_time(P1)
T2 = cells_time(P2)
print(min(abs(x)+abs(y) for x,y in T1 if (x,y) in T2))
print(min(t+T2[p] for p,t in T1.items() if p in T2))
