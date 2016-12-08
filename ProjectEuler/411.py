#!/usr/bin/env python

from bisect import bisect_left

# solution based on the longest increasing subsequence
# O(n log n) but terribly slow, ~20 min with pypy!
# BY FAR my worst time on PE!

# we directly use the tryalgo version here
def longest_increasing_subsequence(x):
    n = len(x)
    p = [None] * n
    h = [None]
    b = [float('-inf')]
    for i in range(n):
        if x[i] > b[-1]:
            p[i] = h[-1]
            h.append(i)
            b.append(x[i])
        else:
            #   -- recherche dichotomique: b[k - 1] < x[i] <= b[k]
            k = bisect_left(b, x[i])
            h[k] = i
            b[k] = x[i]
            p[i] = h[k - 1]
    # extraire solution
    q = h[-1]
    s = []
    while q is not None:
        s.append(x[q])
        q = p[q]
    return s[::-1]

def S(n):
    P = [(pow(2,i,n),pow(3,i,n)) for i in range(2*n)]
    # on trie selon x
    P.sort()
    # on projette sur y en gardant le x pour distinguer les
    # points de meme y ayant des x distincts consecutifs
    P = [(y,x) for (x,y) in P]
    return len(longest_increasing_subsequence(P))

s = 0
for k in xrange(1,31):
    s += S(k**5)
print s
