#!/usr/bin/env python

import sys

N = 10**5+1

def cpt_multiples(A):
    Cpt = [0]*N
    for a in A:
        Cpt[a] += 1
    # Mult[i] contient le nb de multiples de i dans A
    Mult = [sum(Cpt[j] for j in xrange(i,N,i)) if i>0 else 0 for i in xrange(N)]
    return Mult
    
def main():
    n,m,q = map(int,sys.stdin.readline().split())
    A = map(int,sys.stdin.readline().split())
    B = map(int,sys.stdin.readline().split())
    for _ in xrange(q):
        r1,c1,r2,c2 = map(int,sys.stdin.readline().split())
        MA,MB = cpt_multiples(A[r1:r2+1]),cpt_multiples(B[c1:c2+1])
        # DP cpt_gcd[i] = nb de couples (a,b) in AxB tq gcd(a,b) = i
        # cpt_gcd[i] = MA[i]*MB[i] - sum( cpt_gcd(k*i), k>=2 )
        cpt_gcd = [0]*N
        res = 0
        for i in xrange(N-1,0,-1):
            cpt_gcd[i] = MA[i]*MB[i] - sum(cpt_gcd[j] for j in xrange(2*i,N,i))
            if cpt_gcd[i]>0:
                res += 1
        print res

main()
