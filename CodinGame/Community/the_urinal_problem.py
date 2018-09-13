#!/usr/bin/env python3

INF = float('inf')

def left_dist(B):
    D = [0]*len(B)
    l = -INF
    for i in range(len(B)):
        if B[i]=='!':
            l = i
        else:
            D[i] = i-l
    return D

def main():
    N = int(input())
    B = input()
    L = left_dist(B)
    R = left_dist(B[::-1])[::-1]
    D = [min(l,r) for l,r in zip(L,R)]
    print(D.index(max(D)))

main()
