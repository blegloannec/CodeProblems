#!/usr/bin/env python

# very easy one
# a,b,c are roots of kX^3 - k^2X^2 + x - k^3 = 0
# (X-a)(X-b)(X-c) = X^3 - (a+b+c)X^2 + (ab+bc+ac)X - abc
# so that abc = k^2, ab+bc+ac = 1/k, a+b+c = k
# S(n) = sum( Sk(n), k=1..n )
# where Sk(n) = sum( [(ak+bk)(bk+ck)(ck+ak)]^p, p=1..n )
# (a+b)(b+c)(c+a) = (ab+bc+ac)(a+b+c) - abc = 1-k^2
# so Sk(n) = sum( (1-k^2)^p, p=1..n )

P = 10**9+7

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n=P):
    _,u,_ = bezout(a,n)
    return u

def geo_sum(x,a,b):
    return ((pow(x,a,P)-pow(x,b+1,P))*inv_mod(1-x))%P

def main():
    N = 10**6
    S = 0
    for k in xrange(1,N+1):
        x = 1-k*k
        S = (S + geo_sum(x,1,N))%P
    print S

main()
