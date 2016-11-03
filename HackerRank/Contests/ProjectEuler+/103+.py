#!/usr/bin/env python

import sys

def main():
    P = 715827881
    N = int(sys.stdin.readline())
    S = [1,1]
    for i in xrange(N-2):
        if i%2==0:
            S.append((2*S[-1])%P)
        else:
            S.append((2*S[-1]-S[i/2])%P)
    X = [S[N-1]]
    for i in xrange(N-2,-1,-1):
        X.append((X[-1]+S[i])%P)
    print ' '.join(map(str,X))
        
main()
