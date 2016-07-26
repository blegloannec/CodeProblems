#!/usr/bin/env python

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)/p

C = [[-1 for _ in xrange(8)] for _ in xrange(21)]
C[0][0] = 1
for n in xrange(1,21):
    C[n][0] = 0

# C[n][k] = nombre de partitions de n boules en k couleurs
# (avec <=10 boules par couleur)
def DP(n,k):
    if C[n][k]>=0:
        return C[n][k]
    res = 0
    for i in xrange(1,min(n,10)+1):
        res += binom(10,i)*DP(n-i,k-1)
    C[n][k] = res
    return res

print float(sum(i*binom(7,i)*DP(20,i) for i in xrange(2,8)))/binom(70,20)
# solution a 9 decimales : 6.818741802
