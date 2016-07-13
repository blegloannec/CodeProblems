#!/usr/bin/env python

def fact(n):
    return 1 if n<2 else n*fact(n-1)

# compte les tirages a exactement k bleus
memo = {}
def cpt(n,b):
    if n==0:
        return 1 if b==0 else 0
    if (n,b) in memo:
        return memo[n,b]
    res = n*cpt(n-1,b)+cpt(n-1,b-1)
    memo[n,b] = res
    return res

def main():
    N = 15
    t,w = fact(N+1),sum(cpt(N,p) for p in xrange(N/2+1,N+1))
    print (t-w)/w+1

main()
