#!/usr/bin/env python3

# Idea: Symmetric strategy
# There are only 3 moves that are self-symmetric for the
# board central symmetry:
#   (3,c)--(3,7-c) for c = 1,2,3
# all of which are forbidden after the (3,1)-(3,6) move.
# Hence, starting with this move, we force the opponent to
# play on a central-symmetric board without self-symmetric move
# and we can always symmetrize each of its moves until the board
# is filled.

import sys
input = sys.stdin.readline

def send_recv(r1,c1, r2,c2):
    sys.stdout.write(f'{r1} {c1} {r2} {c2}\n')
    sys.stdout.flush()
    return input().strip()

def game():
    A = send_recv(3,1, 3,6)
    while A!='GAME':
        r1,c1,r2,c2 = map(int, A.split()[1:])
        A = send_recv(6-r2,7-c2, 6-r1,7-c1)

def main():
    N = int(input())
    for _ in range(N):
        game()

main()
