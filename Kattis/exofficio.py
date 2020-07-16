#!/usr/bin/env python3

import sys

# The optimal is always obtained by using only horiz. or vert. lines
# and cutting them in half in the middle in the other direction
# (like drawing two "combs" face to face).
# However, when that cutting dimension is even, we cannot cut exactly
# in the middle, thus creating an unbalanced situation (which cannot
# be avoided when both dimensions are even).
# Hence when there is exactly one even and one odd dimension,
# we should always draw the lines along the odd dimension to be
# able to cut them exactly in half in the other direction.
# Example: for 3 2
#  _ _ _                    _ _ _
# |_   _|  is better than  | | | |
# |_ _ _|                  |_ _ _|

def main():
    H,W = map(int, sys.stdin.readline().split())
    G = [' _'*W]  # /!\ no extra space at the end!
    if H%2==1:
        G += ['| '*W+'|' for _ in range(H-1)]
        G.append('|_'*W+'|')
        G[H//2+1] = '|' + G[H//2+1][1:-1].replace('|',' ') + '|'
    else:
        G += [['|','_']+[' ','_']*(W-1)+['|'] for _ in range(H)]
        for i in range(1,H):
            G[i][2*(W//2)+1] = ' '
        G = [''.join(L) for L in G]
    sys.stdout.write('\n'.join(G))
    sys.stdout.write('\n')

main()
