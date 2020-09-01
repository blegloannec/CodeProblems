#!/usr/bin/env python3

import sys

#           ┌───┬─┰─┐
# ┌─┰─┐     │1┏━┥0┗━┥
# │0┗━┥ --> ├─╂─┼─┰─┤ + rotations
# └───┘     │0┗━┿━┛3│
#           └───┴───┘

S = ((0,3,1,0), (0,1,1,2), (2,3,1,2), (0,3,3,2))
H = (3,1,0,2)  # "isolated corners" of each tile

def main():
    N = int(sys.stdin.readline())
    for _ in range(N):
        x,y = map(int, sys.stdin.readline().split())
        l = max(x.bit_length(), y.bit_length())
        c = o = 0  # tile & orientation
        for n in range(l, -1, -1):
            p = (((y>>n)&1)<<1) | ((x>>n)&1)
            # the orientation is either defined by the current tile,
            # or, in the isolated corner case, is inherited from the parent
            if p!=H[c]:
                o = c
            # new current tile
            c = S[c][p]
        sys.stdout.write(f'{o}\n')

main()
