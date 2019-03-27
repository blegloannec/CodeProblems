#!/usr/bin/env python3

def equalize(A,B):
    O = []
    r, R = 0, []
    for i in range(len(A)):
        if r>0 and A[i]>=r:
            A[i] -= r
            O += R[::-1]
            r, R = 0, []
        d = B[i]-A[i]
        if r==0 and d<0:
            A[i+1] -= d
            O.append((i+1,1,-d))
        elif r>0 or d>0:
            r += d
            R.append((i+2,-1,r))
    return O

if __name__=='__main__':
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    O = equalize(A,B)
    print(len(O))
    for o in O:
        print(*o)
