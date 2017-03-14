#!/usr/bin/env python3

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input())))
B = []
for _ in range(N):
    B.append(list(map(int,input())))
for i in range(N):
    for j in range(N):
        A[i][j] += B[i][j]

modif = True
while modif:
    modif = False
    for i in range(N):
        for j in range(N):
            if A[i][j]>=4:
                modif = True
                A[i][j] -= 4
                for (x,y) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=x<N and 0<=y<N:
                        A[x][y] += 1

for L in A:
    print(''.join(map(str,L)))
