#!/usr/bin/env python3

# O(N^2) time, O(N) space
def square_count(P):
    N = len(P)
    S = set(P)
    cpt = 0
    for i in range(N):
        for j in range(i+1,N):
            (xi,yi),(xj,yj) = (P[i],P[j]) if P[i]<P[j] else (P[j],P[i])
            # two parallel sides of a square will always be oriented
            # the same way, hence the square will be discovered by
            # exactly one of them
            # then each square is counted twice (once for each pair of
            # opposite sides
            dx,dy = xi-xj,yi-yj
            nx,ny = -dy,dx  # checking only one side of the edge
            if (xi+nx,yi+ny) in S and (xj+nx,yj+ny) in S:
                cpt += 1
    return cpt//2

def main():
    N = int(input())
    P = [tuple(map(int,input().split())) for _ in range(N)]
    print(square_count(P))

main()
