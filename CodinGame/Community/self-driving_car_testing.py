#!/usr/bin/env python3

N = int(input())
Com = input().split(';')
X,Cmd = int(Com[0])-1,Com[1:]
Road = []
for _ in range(N):
    r,road = input().split(';')
    Road += [list(road) for _ in range(int(r))]

Dir = {'L':-1, 'S':0, 'R':1}
Y = 0
for C in Cmd:
    DX = Dir[C[-1]]
    for _ in range(int(C[:-1])):
        X += DX
        Road[Y][X] = '#'
        Y += 1
print('\n'.join(''.join(L) for L in Road))
