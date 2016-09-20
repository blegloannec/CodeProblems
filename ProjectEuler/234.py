#!/usr/bin/env python

from math import sqrt

# si p<q sont 2 nb premiers consecutifs
# les nb p^2 < x < q^2 verifient lps(x) = p
# et ups(x) = q
# on peut facilement compter les multiples de
# p et de q parmi ces nombres, puis retirer (2 fois)
# les multiples de ppcm(p,q) = p*q

def sieve_list(N):
    P = [True for _ in xrange(N)]
    L = []
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
    return L

def sum_mult(n,a,b):
    x = (a+n-1)/n
    y = b/n
    return n*(x+y)*(y-x+1)/2

def main():
    N = 999966663333
    P = sieve_list(int(sqrt(N))+100)
    S = 0
    for i in xrange(len(P)-1):
        p,q = P[i],P[i+1]
        A,B = p*p+1,min(q*q-1,N)
        if A>N:
            break
        S += sum_mult(p,A,B)+sum_mult(q,A,B)-2*sum_mult(p*q,A,B)
    print S

main()
