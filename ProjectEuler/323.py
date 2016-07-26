#!/usr/bin/env python

# pour 1 bit :
# X = nb de tirages pour tomber sur 1
# P[X=k] = 1/2^k
# P[X<=n] = sum( P[k], k=1..n ) = (1/2 - 1/2^(n+1))/(1/2 - 1)

# pour 32 bits :
# Y = nb de tirages pour n'avoir plus que des 1
# P[Y>n] = 1 - P[X<=n]^32
# P[Y=n] = P[Y>n-1]-P[Y>n]
# E[Y] = sum( n*P[Y=n] ) = sum( n*P[Y>n-1] - n*P[Y>n] ) = sum( P[Y>n] )

def P(k):
    return 1 - ((0.5-(0.5)**(k+1))/(1-0.5))**32

print sum((P(k)) for k in xrange(1000))
