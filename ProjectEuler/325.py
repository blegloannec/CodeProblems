#!/usr/bin/env python

from math import sqrt

## EXPERIMENTS CODE
N = 1001
W = [[None for _ in xrange(N)] for _ in xrange(N)]
def win(S,L):
    if S==0:
        return False
    if W[S][L]!=None:
        return W[S][L]
    for k in xrange(S,L+1,S):
        l = L-k
        if not win(min(S,l),max(S,l)):
            W[S][L] = True
            return True
    W[S][L] = False
    return False

# by printing the win/lose matrix, we guess that
# (S,L), S<L, is a losing position iff S/L > 1/phi
# where phi = (1+sqrt(5))/2 is the golden ratio
# (while the limit case S=L is a winning position)
# https://oeis.org/A000201
def experiments():
    ratios = []
    print N-2
    for i in xrange(2,N):
        cpt = 0
        for j in xrange(1,i):
            if win(j,i):
                cpt += 1
            #print int(win(j,i)),
        #print
        ratios.append(float(cpt)/i)
    print ratios

# experiments()


## ACTUAL SOLUTION
# we re-use our code for CodeChef problem Euler Sum
# cf. JuneChallenge17/es.py for explanations
# here the limit word is the Fibonacci word
# https://oeis.org/A005614

# tailles et sommes des mots s(n)
Size = [1,1,1]
Sums = [1,0,1]
for i in xrange(100):
    Size.append(Size[-1] + Size[-2])
    Sums.append(Sums[-1] + Sums[-2])

# nb d'elements par triangle
memo0 = {}
def _ST0(k,n):
    if k<=2:
        return 0
    if (k,n) in memo0:
        return memo0[k,n]
    if n<=Size[k-1]:
        res = _ST0(k-1,n)
    else:
        m = n-Size[k-1]
        res = m*Sums[k-1] + _ST0(k-1,Size[k-1]) + _ST0(k-2,m)
    memo0[k,n] = res
    return res

# somme des coordonnees des points des triangles
# (i.e. sum x+y for sub-diagonal x<=y winning positions)
memo = {}
def _ST(k,n):
    if k<=2:
        return 0
    if (k,n) in memo:
        return memo[k,n]
    if n<=Size[k-1]:
        res = _ST(k-1,n)
    else:
        m = n-Size[k-1]
        res = Size[k-1]*m*Sums[k-1] + m*(m+1)/2*Sums[k-1] + m*Sums[k-1]*(Sums[k-1]+1)/2 + _ST(k-1,Size[k-1]) + _ST0(k-2,m)*(Size[k-1]+Sums[k-1]) + _ST(k-2,m)
    memo[k,n] = res
    return res

def ST(n):
    k = 0
    while Size[k]<n:
        k += 1
    return _ST(k,n)

def sub_diag_sum(n):
    return (n-1)*n*(n+1)/2

n = 10**16
print (sub_diag_sum(n) - ST(n)) % 7**10
