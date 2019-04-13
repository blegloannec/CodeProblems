#!/usr/bin/env pypy2

import sys

H = 18
# N = 6 is enough
P = [2**4, 3**2, 7, 11, 13, 17]  # PPCM(P) = 2 450 448 > 10^6

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

def send(S):
    print S
    sys.stdout.flush()

def case():
    M, p = 0, 1
    for q in P:
        send(' '.join([str(q)]*H))
        m = sum(map(int,raw_input().split())) % q
        M = rev_chinois(M,p,m,q)
        p *= q
    send(str(M))
    assert raw_input()=='1'

if __name__=='__main__':
    T,_,_ = map(int,raw_input().split())
    for _ in xrange(T):
        case()
