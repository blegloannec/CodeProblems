#!/usr/bin/env pypy

# weak approach...

import array

def pattern_edit(u,v):
    m,n = len(u),len(v)
    T = [array.array('H',[0]*(n+1)) for _ in xrange(m+1)]
    for i in xrange(m+1):
        T[i][0] = 0
    for j in xrange(1,n+1):
        T[0][j] = j
    for i in xrange(1,m+1):
        for j in xrange(1,n+1):
            T[i][j] = min(T[i-1][j]+1,T[i][j-1]+1,T[i-1][j-1]+int(u[i-1]!=v[j-1]))
    return T

def std_edit(u,v):
    m,n = len(u),len(v)
    T = [array.array('H',[0]*(n+1)) for _ in xrange(m+1)]
    for i in xrange(m+1):
        T[i][0] = i
    for j in xrange(1,n+1):
        T[0][j] = j
    for i in xrange(1,m+1):
        for j in xrange(1,n+1):
            T[i][j] = min(T[i-1][j]+1,T[i][j-1]+1,T[i-1][j-1]+int(u[i-1]!=v[j-1]))
    return T

def main():
    k = int(raw_input())
    P = raw_input()
    Pinv = P[::-1]
    G = raw_input()
    T = pattern_edit(G,P)
    for i in xrange(len(G)+1):
        if T[i][len(P)]<=k:
            i0 = max(0,i-len(P)-k-1)
            Ginv = G[i-1::-1] if i0==0 else G[i-1:i0:-1]
            T2 = std_edit(Ginv,Pinv)
            for j in xrange(len(Ginv)+1):
                if T2[j][len(P)]<=k:
                    print i-j+1,j

main()
