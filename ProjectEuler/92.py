#!/usr/bin/env python

# si n < 10^7
# alors succ(n) <= 7*9^2 <= 567

def succ(n):
    s = 0
    while n>0:
        c = n%10
        s += c*c
        n /= 10
    return s

def chain(x):
    if X[x]>0:
        return X[x]
    x0 = chain(succ(x))
    X[x] = x0
    return x0
    
def main():
    global X
    N = 568
    X = [0 for i in xrange(N)]
    X[1] = 1
    X[89] = 89
    cpt = 0
    for i in xrange(1,N):
        if chain(i)==89:
            cpt += 1
    for i in xrange(N,10000000):
        if X[succ(i)]==89:
            cpt += 1
    print cpt

main()
