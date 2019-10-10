#!/usr/bin/env python3

from collections import deque

S = 5
V = ((-1,-2),(-2,-1),(1,-2),(-2,1),(1,2),(2,1),(-1,2),(2,-1))

def hole(C):
    p = 0
    while True:
        if C&3==2:
            return p
        C >>= 2
        p += 1

def swap(C,a,b):
    a <<= 1
    b <<= 1
    c = ((C>>a)&3) ^ ((C>>b)&3)
    return C ^ ((c<<b) | (c<<a))

def bfs(max_dist=10):
    # 00 = white, 01 = black, 10 = hole, 11 = invalid
    C0 = 0b00000000000100000000010110000001010101000101010101
    Dist = {C0: 0}
    Q = deque([C0])
    while Q:
        C = Q.popleft()
        if Dist[C]>=max_dist:
            continue
        h = hole(C)
        i,j = divmod(h,S)
        for vi,vj in V:
            if 0<=i+vi<S and 0<=j+vj<S:
                k = S*(i+vi) + j+vj
                D = swap(C,h,k)
                if D not in Dist:
                    Dist[D] = Dist[C] + 1
                    Q.append(D)
    return Dist

def main():
    Code = {'0':0, '1':1, ' ':2}
    Dist = bfs()
    N = int(input())
    for _ in range(N):
        I = ''.join(input() for _ in range(S))
        C = 0
        for c in reversed(I):
            C = (C<<2) | Code[c]
        if C in Dist:
            print('Solvable in %d move(s).' %  Dist[C])
        else:
            print('Unsolvable in less than 11 move(s).')

main()
