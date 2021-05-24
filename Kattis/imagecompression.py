#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    H,W = map(int, input().split())
    I = [list(map(int, input().split())) for _ in range(H)]
    O = lambda i,j: I[i][j] if i>=0 and j>=0 else 0
    C = [0]*256
    for i in range(H):
        N = [0]*256
        S = [0]*256
        U = [0]*256
        A = [0]*256
        for j in range(W):
            N[O(i,j)] += 1
            S[(O(i,j) - O(i,j-1)) % 256] += 1
            U[(O(i,j) - O(i-1,j)) % 256] += 1
            A[(O(i,j) - ((O(i-1,j)+O(i,j-1))%256)//2) % 256] += 1
        for x in range(256):
            C[x] += max(N[x],S[x],U[x],A[x])
    xmax = 255
    for x in range(254,-1,-1):
        if C[x]>C[xmax]:
            xmax = x
    print(xmax, C[xmax])

main()
