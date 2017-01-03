#!/usr/bin/env python

import sys

# https://en.wikipedia.org/wiki/Lazy_caterer%27s_sequence
# https://oeis.org/A000124
# en ne gardant que les termes d'indices pairs ici (on place 2 lignes
# a la fois)

def main():
    q = int(sys.stdin.readline())
    for _ in xrange(q):
        n = 2*int(sys.stdin.readline())
        print n*(n-1)/2+1

main()
