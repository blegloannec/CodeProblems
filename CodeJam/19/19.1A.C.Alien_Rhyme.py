#!/usr/bin/env pypy2

# O(N^2 * L) good enough approach (N ~ 1000 and L ~ 50 the size of the words).
# Can be reduced to O(N*L) replacing the suffixes hashtable by a trie stocking
# reversed words + a recursive computation of the result (see official analysis),
# yet the implementation is significantly more complicated.

from collections import defaultdict

def main():
    T = int(raw_input())
    for t in xrange(1,T+1):
        N = int(raw_input())
        W = [raw_input() for _ in xrange(N)]
        Suff = defaultdict(list)
        for i in xrange(N):
            for s in xrange(len(W[i])):
                Suff[W[i][s:]].append(i)
        L = sorted((w for w in Suff if len(Suff[w])>1), key=(lambda w: -len(w)))
        Used = [False]*N
        res = 0
        for w in L:
            S = [i for i in Suff[w] if not Used[i]]
            if len(S)>=2:
                res += 2
                Used[S[0]] = True
                Used[S[1]] = True
        print('Case #%d: %d' % (t,res))

main()
