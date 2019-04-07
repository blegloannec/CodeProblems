#!/usr/bin/env python3

if __name__=='__main__':
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        P = input()
        S = ''.join('ES'[c=='E'] for c in P)
        print('Case #%d: %s' % (t,S))
