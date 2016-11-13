#!/usr/bin/env python

# (x+y+z)^n = sum( multinom(n,a,b,c)*x^a*y^b*z^c, a+b+c=n )
# multinom(n,a,b,c) = n! / (a! b! c!)

# runs in 58s with pypy

def fact_power(n,p):
    res = 0
    q = p
    while q<=n:
        res += n/q
        q *= p
    return res

def main():
    N,L = 200000,12
    P2 = [fact_power(n,2) for n in xrange(N+1)]
    P5 = [fact_power(n,5) for n in xrange(N+1)]
    cpt = 0
    for a in xrange(N+1):
        for b in xrange(a,N+1):
            c = N-a-b
            if c<b:
                break
            if min(P2[N]-P2[a]-P2[b]-P2[c],P5[N]-P5[a]-P5[b]-P5[c])>=L:
                if a==b==c:
                    cpt += 1
                elif a==b or b==c or a==c:
                    cpt += 3
                else:
                    cpt += 6
    print cpt

main()
