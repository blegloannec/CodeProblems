#!/usr/bin/env python3

# DP to guess the pattern
from functools import lru_cache
@lru_cache(maxsize=None)
def win(n0, n1, n2, first=True):
    assert n0>=0 and n1>=0 and n2>=0
    if n0+n1+n2==1:
        if n1==1:
            return first
        if n2==1:
            return not first
        return False
    if n0>1 and not win(n0-1, n1, n2, not first):
        return True
    if n1>1 and not win(n0+1, n1-2, n2, not first):
        return True
    if n2>1 and not win(n0+1, n1, n2-2, not first):
        return True
    if n0>0 and n1>0 and (not win(n0-1, n1, n2, not first) or \
                          not win(n0-1, n1-1, n2+1, not first)):
        return True
    if n0>0 and n2>0 and (not win(n0-1, n1, n2, not first) or \
                          not win(n0-1, n1+1, n2-1, not first)):
        return True
    if n1>0 and n2>0 and (not win(n0, n1, n2-1, not first) or \
                          not win(n0, n1-1, n2, not first)):
        return True
    return False

def experiment():
    N = [0]*3
    for n in range(2,100):
        N[n%3] += 1
        assert win(*N)==(n%2==1)
        #print(n, win(*N))

#experiment()
# we discover that the result is simply determined by the parity of n
# (This can actually easily be proved: Let us consider the last turn,
#  there are 2 remaining values x and y and the player has to choose
#  x-y or y-x mod 3. If x = y, then x-y = y-x = 0 and the player wins.
#  Otherwise, we always have {x-y,y-x} = {1,2} mod 3 and the player can
#  simply pick the right one to win. The last player always win!)

import sys
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        sys.stdout.write('Kitty\n' if N==1 or N&1==0 else 'Katty\n')

main()
