#!/usr/bin/env python3

import sys

def win(n, memo, p=1, first=True):
    if p>=n:
        return not first
    key = (p,first)
    if key not in memo:
        if first:
            memo[key] = any(win(n, memo, p*d, not first) for d in range(2,10))
        else:
            memo[key] = all(win(n, memo, p*d, not first) for d in range(2,10))
    return memo[key]

# there is a pattern!
# http://oeis.org/A067421
def pattern(n):
    i = 0
    x = 2
    while True:
        x += 8*18**i
        if x>n:
            return True
        x += x-1
        if x>n:
            return False
        i += 1

def main():
    for L in sys.stdin.readlines():
        N = int(L)
        #print('Stan' if win(N,{}) else 'Ollie', 'wins.')
        print('Stan' if pattern(N) else 'Ollie', 'wins.')

main()
