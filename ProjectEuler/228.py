#!/usr/bin/env python3

from fractions import *

# https://en.wikipedia.org/wiki/Minkowski_addition
# The Minkowsky sum of two convex polygons is a convex
# polygon whose "border" is simply obtained by taking the
# polar-angle ordered sequence of edges from both original
# polygons.
# Hence its perimeter is exactly the sum of both perimeters.
# And when two original edges have the same polar-angle
# they are "concatenated" into one single edge in the resulting
# polygon.
# So this is all about counting unique fractions (as in Farey
# sequences related problems 71-73) but in such a small range
# of denominators that we do not bother with any arithmetical
# consideration here and just implement a "naive" solution.

# It's a complete mystery why this problem has a 70% difficulty
# rating?!

def edge_angles(n):
    return set([Fraction(k,n) for k in range(n)])

def main():
    E = set()
    for i in range(1864,1910):
        E |= edge_angles(i)
    print(len(E))

main()
