#!/usr/bin/env python3

# kinda half-queens problem:
#   find a max number of positions (x,y), z := n-x-y, 0 <= x,y,z <= n
#   such that x/y/z-coordinates are all distinct (horizontal, vertical,
#   and one direction of diagonals) on a half-square (n+1)^2 as
#   (as 0 <= z <= n  <=>  0 <= x+y <= n)

def build_set(n):
    # optimal starting position (could also be brute-forced)
    j0 = (n+1)//3 - (n+1)%3 + 1  # http://oeis.org/A063942
    C = []
    i,j = 0,j0
    while i<=n-j:
        C.append((i,j))
        i += 1
        j += 1
    j = 0
    while i<=n-j and j<j0:
        C.append((i,j))
        i += 1
        j += 1
    return C

if __name__=='__main__':
    N = int(input())
    S = build_set(N)
    print(len(S))
    for a,b in S:
        print(a, b, N-a-b)
