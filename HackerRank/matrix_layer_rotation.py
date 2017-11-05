#!/usr/bin/env python3

def pos2num(h,w,i,j):
    h -= 1
    w -= 1
    if j==0:
        return i
    if i==h:
        return h+j
    if j==w:
        return 2*h+w-i
    return 2*h+2*w-j

def num2pos(h,w,n):
    if n<h:
        return (n,0)
    if n<h+w-1:
        return(h-1,n-h+1)
    if n<2*h+w-2:
        return (2*h+w-3-n,w-1)
    return (0,2*h+2*w-4-n)


def rotate(M,X):
    H,W = len(M),len(M[0])
    R  = [L[:] for L in M]
    for i in range(H):
        L = []
        for j in range(W):
            c = min(i,H-1-i,j,W-1-j)
            h,w = H-2*c,W-2*c
            if h>1 and w>1:
                l = 2*h+2*w-4
                x,y = num2pos(h,w,(pos2num(h,w,i-c,j-c)+X)%l)
                x += c
                y += c
                R[x][y] = M[i][j]
    return R
                
def main():
    H,W,R = map(int,input().split())
    M = [input().split() for _ in range(H)]
    R = rotate(M,R)
    for L in R:
        print(' '.join(L))

main()
