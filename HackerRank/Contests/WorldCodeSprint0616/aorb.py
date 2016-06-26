#!/usr/bin/env python

import sys

def parse(x,S):
    R = [0 for _ in xrange(S)]
    i = 0
    while 8*i<len(x):
        R[i] = int(x[max(0,len(x)-8*(i+1)):len(x)-8*i],16)
        i += 1
    return R

def gb(X,n):
    return (X[n/32]>>(n%32))&1

def sb(X,n):
    X[n/32] ^= 1<<(n%32)

def affich(X):
    s = []
    k = len(X)-1
    while k>=0 and X[k]==0:
        k -= 1
    if k<0:
        return '0'
    s.append(('%X'%X[k]).upper())
    for i in xrange(k-1,-1,-1):
        s.append(('%08X'%X[i]).upper())
    return ''.join(s)

def main():
    Q = int(sys.stdin.readline())
    for _ in xrange(Q):
        K = int(sys.stdin.readline())
        A = sys.stdin.readline().strip()
        B = sys.stdin.readline().strip()
        C = sys.stdin.readline().strip()
        S = max(len(A),len(B),len(C))/8+1
        A = parse(A,S)
        B = parse(B,S)
        C = parse(C,S)
        for i in xrange(32*S-1,-1,-1):
            a,b,c = gb(A,i),gb(B,i),gb(C,i)
            if (a,b,c)==(0,1,0):
                sb(B,i)
                K -= 1
            elif (a,b,c)==(1,0,0):
                sb(A,i)
                K -= 1
            elif (a,b,c)==(1,1,0):
                sb(A,i)
                sb(B,i)
                K -= 2
            elif (a,b,c)==(0,0,1):
                sb(B,i)
                K -= 1
            if K<0:
                print -1
                break
        if K>0:
            for i in xrange(32*S-1,-1,-1):
                a,b = gb(A,i),gb(B,i)
                if (a,b)==(1,1):
                    sb(A,i)
                    K -= 1
                elif (a,b)==(1,0) and K>=2:
                    sb(A,i)
                    sb(B,i)
                    K -= 2
                if K==0:
                    break
        if K>=0:
            print affich(A)
            print affich(B)

main()
