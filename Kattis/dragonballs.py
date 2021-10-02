#!/usr/bin/env python3

# interactive problem!

# Obviously there are lots of possible approaches...
# Here we simply consider that with very high probability,
# two close-enough (e.g. adjacent) cells will have the same
# closest ball and we can then always identify a remaining
# ball with only 3 or 4 requests (which is way more efficient
# than needed).

# let d² and e² the answers from (x0,y0) and (x0+1,y0)
# assume (x,y) is the closest ball
# d² = (x-x0)²   + (y-y0)²
# e² = (x-x0-1)² + (y-y0)²
#    = (x-x0)² - 2(x-x0) + 1 + (y-y0)²
# d²-e² = 2(x-x0)-1
# x = x0 + (d²-e²+1)/2
# y = y0 ± √(d²-(x-x0)²)

import sys, random
random.seed()
from math import sqrt

S = 10**6

input = sys.stdin.readline
def send_recv(x,y):
    sys.stdout.write(f'{x} {y}\n')
    sys.stdout.flush()
    return int(input())

def main():
    N = int(input())
    while N>0:
        x0 = random.randint(0, S-1)
        y0 = random.randint(0, S)
        d2 = send_recv(x0, y0)
        e2 = send_recv(x0+1, y0)
        if (d2-e2+1)%2 == 0:
            x = x0 + (d2-e2+1)//2
            if 0 <= x <= S:
                s = d2 - (x-x0)**2
                r = round(sqrt(s))
                if r*r == s:
                    for y in (y0-r, y0+r):
                        if 0 <= y <= S:
                            if send_recv(x, y) == 0:
                                N -= 1
                                break

main()
