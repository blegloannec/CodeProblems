#!/usr/bin/env python

# n^2+k for k in [1,3,7,9,13,27] must be consecutive primes
# then n is even and n^2+k for k in [5,11,15,17,19,21,23,25] are composite
# to reduce the n to test:
# - if n = 0 mod 3  then n^2+3 = n^2+9 = n^2+27 = 0 mod 3 so n%3!=0
# - if n = 1,4 mod 5 then n^2 = 1 mod 5 and n^2+9 = 0 mod 5
#   and if n = 2,3 mod 5 then n^2+1 = 0 mod 5 so n%5==0
#   so n%10==0 as n is even
# - if n = 0 mod 7 then n^2+7 = 0 mod 7
#   and if n = 1,6 mod 7 then n^2 = 1 mod 7 and n^2+13 = 0 mod 7
#   and if n = 2,5 mod 7 then n^2 = 4  mod 7 and n^2+3 = 0 mod 7
#   so n%7==3 or 4
# moreover as n%5==0, n^2+{5,15,25} are always composite
# and as n != 0 mod 3 then n^2 = 1 mod 3 and n^2+{11,17,23} are always composite
# and as n = 3,4 mod 7 then n^2 = 2 mod 7 and n^2+19 is always composite

# runs in 33s with pypy

# Miller-Rabin deterministe 64 bits
def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def witness(a,n,b):
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n):
    b = digits(n-1,2)
    for w in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True

def test(n):
    for (k,B) in [(1,True),(3,True),(7,True),(9,True),(13,True),(21,False),(27,True)]:
        if miller_rabin(n+k)!=B:
            return False
    return True

def main():
    N = 150*10**6
    S = 0
    for n in xrange(10,N,10):
        if n%3!=0 and 3<=n%7<=4 and test(n*n):
            S += n
    print S

main()
