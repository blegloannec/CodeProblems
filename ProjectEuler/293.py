#!/usr/bin/env python

P = [2,3,5,7,11,13,17,19,23]
N = 10**9

def gen_admissible(i=0,n=1):
    if i<len(P):
        n *= P[i]
        while n<=N:
            yield n
            for a in gen_admissible(i+1,n):
                yield a
            n *= P[i]

# Miller-Rabin deterministe 32 bits
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
    for w in [2,7,61]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True

def main():
    PF = set()
    for n in gen_admissible():
        m = 3
        while not miller_rabin(n+m):
            m += 2
        PF.add(m)
    print sum(PF)

main()
