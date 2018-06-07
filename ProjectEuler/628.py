#!/usr/bin/env pypy

# pawns form a permutation matrix
# a configuration is blocked (not open) iff there
# exists a completely blocked diagonal
# there is at most one blocked diagonal in the bottom-left
# half of the matrix and at most one in the top-right half

# . . . . . . X .
# . . . . . . . X
# . . . ? ? ? . .
# . . . ? ? ? . .
# . . . ? ? ? . .
# X . . . . . . .
# . X . . . . . .
# . . X . . . . .

N = 10**8
P = 1008691207

# factorials
F = [1]*(N+1)
for n in xrange(1,N+1):
    F[n] = (n*F[n-1]) % P

def blocked(n):
    res = -1
    for i in xrange(1,n+1):
        #   diagonal of size i in the bottom-left half
        # +                           top-right
        # - 2 diagonals of size a in bottom-left half
        #                   and b    top-right
        #   such that a+b = i
        res = (res + (2-(i-1))*F[n-i]) % P
    return res

print (F[N]-blocked(N))%P
