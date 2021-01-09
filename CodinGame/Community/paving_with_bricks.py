#!/usr/bin/env python3

# much simpler version of Kattis/macarons.cpp 

from functools import lru_cache

W = int(input())
H = int(input())
if W<H:
    W,H = H,W
# then H <= 7 (as W*H <= 50)

# backtracking to generate previous borders in O(2^H)
# R is the mask of size H of the current vertical border
# 1s indicate positions where a domino crosses the border
#      L R
#   ?  |?|<=>  0
#   0  |<=>    1
#   ?  |?|^    0
#   ?  |?|v    0
def _prev_borders(R, i=0, L=0):
    if i==H:
        yield L
    elif (R>>i)&1:
        # pos. already occupied by an horiz. domino (crossing R)
        yield from _prev_borders(R, i+1, L)
    else:
        if i+1<H and (R>>(i+1))&1==0:
            # we put a vertical domino in i and i+1
            yield from _prev_borders(R, i+2, L)
        # we put a horizontal domino in i (crossing L)
        yield from _prev_borders(R, i+1, L|(1<<i))

# memoized version of the backtracking
@lru_cache(maxsize=None)
def prev_borders(R):
    return tuple(_prev_borders(R))

# counting in O(W * 2^H) in total
# NB1: O(log W * 2^(3H)) is also possible using matrix exponentiation
# NB2: There is a O(H*W) floating-point formula (see https://oeis.org/A099390
#      or https://en.wikipedia.org/wiki/Domino_tiling )
@lru_cache(maxsize=None)
def count(w=W, border=0):
    if w==0:
        return 1 if border==0 else 0
    return sum(count(w-1, left) for left in prev_borders(border))

print(0 if W&1==H&1==1 else count())
