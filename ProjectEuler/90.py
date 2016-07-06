#!/usr/bin/env python

# naive solution (brute-force on all possible dice)

# sous ensembles de taille n de 
def parmi(n,p):
    if p==0:
        yield []
    else:
        for i in xrange(p-1,n):
            for S in parmi(i,p-1):
                S.append(i)
                yield S

def f69(c):
    return 6 if c==9 else c

def decomp(n):
    return (f69(n/10),f69(n%10))

def CinD(c,D):
    res = c in D
    if c==6:
        res |= 9 in D
    return res

def test(S,D1,D2):
    for (a,b) in S:
        if not ((CinD(a,D1) and CinD(b,D2)) or (CinD(b,D1) and CinD(a,D2))):
            return False
    return True

def main():
    N = 9
    S = [decomp(i*i) for i in xrange(1,N+1)]
    cpt = 0
    for D1 in parmi(10,6):
        for D2 in parmi(10,6):
            if test(S,D1,D2):
                cpt += 1
    print cpt/2

main()
