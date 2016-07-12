#!/usr/bin/env python

# C(n,a,l) = nb mots de taille n se terminant par a<=2 "A"
# et utilisant exactement l "L"
# (et dont tous les blocs de A sont de taille <=2)
memo = {}
def C(n,a,l):
    if n==0:
        return 1 if a==l==0 else 0
    if (n,a,l) in memo:
        return memo[n,a,l]
    c = 0
    # terminer par A
    if a>0:
        c += C(n-1,a-1,l)
    else:
        # terminer par O
        c += C(n-1,0,l)+C(n-1,1,l)+C(n-1,2,l)
        # terminer par L
        if l>0:
            c += C(n-1,0,l-1)+C(n-1,1,l-1)+C(n-1,2,l-1)
    memo[n,a,l] = c
    return c

def main():
    N = 30
    print sum(C(N,a,0)+C(N,a,1) for a in xrange(3))

main()
