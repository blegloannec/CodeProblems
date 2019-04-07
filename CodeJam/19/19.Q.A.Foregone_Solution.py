#!/usr/bin/env python3

def phourbia(N):
    B = N.replace('4','3')
    A = ''.join('01'[c=='4'] for c in N).lstrip('0')
    return A,B

if __name__=='__main__':
    T = int(input())
    for t in range(1,T+1):
        N = input()
        A,B = phourbia(N)
        print('Case #%d: %s %s' % (t,A,B))
