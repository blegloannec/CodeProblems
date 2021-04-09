#!/usr/bin/env python3

# 534
# 912
# 867

No = [ 5, 3, 4, 2, 7, 6, 8, 9]
DI = [-1,-1,-1, 0, 1, 1, 1, 0]
DJ = [-1, 0, 1, 1, 1, 0,-1,-1]

S = int(input())
Img = [list(map(int, input().split())) for _ in range(S)]
Out = [L.copy() for L in Img]
for i in range(S):
    for j in range(S):
        if Img[i][j]==1:
            s = sum(Img[i+DI[l]][j+DJ[l]] for l in range(-3,2))
            for k in range(8):
                s += Img[i+DI[(k+2)%8]][j+DJ[(k+2)%8]]-Img[i+DI[k-3]][j+DJ[k-3]]
                if s==0:
                    Out[i+DI[k]][j+DJ[k]] = No[k]
for L in Out:
    print(*L)
