#!/usr/bin/env python

import sys

def couples(A,i):
    # nb couples W <= X <= i avec W <= A
    return i*(i+1)/2 if i<=A else A*(A+1)/2+(i-A)*A

def main():
    A,B,C,D = sorted(map(int,sys.stdin.readline().split()))
    # A <= B <= C <= D
    # on s'imposera aussi W <= X <= Y <= Z
    # on commence avec les couples (W,X) en O(A*B)
    # DWX[x][i] le nb de couples W<=A, X<=i et W<=X tels que W^X = x
    DWX = {}
    for W in xrange(1,A+1):
        for X in xrange(W,B+1):
            x = W^X
            if x in DWX:
                DWX[x][X] += 1
            else:
                DWX[x] = [0 for _ in xrange(B+1)]
                DWX[x][X] = 1
    for x in DWX:
        for i in xrange(1,B+1):
            DWX[x][i] += DWX[x][i-1]
    c = 0
    for Y in xrange(1,C+1):
        for Z in xrange(Y,D+1):
            # pour former 0, il faut X^Y = Y^Z
            # il y a donc DWX[x][min(Y,B)] choix pour W et X formant 0
            x = Y^Z
            c += couples(A,min(Y,B)) # tous les choix pour W et X
            if x in DWX: # moins les choix formant 0
                c -= DWX[x][min(Y,B)]
    print c

main()
