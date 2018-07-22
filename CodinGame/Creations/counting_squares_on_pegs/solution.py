#!/usr/bin/env python3

# O(N^2) time, O(N) space
def square_count(P):
    N = len(P)
    S = set(P)
    cpt = 0
    for i in range(N):
        xi,yi = P[i]
        for j in range(i+1,N):
            xj,yj = P[j]
            dx,dy = xi-xj,yi-yj
            for nx,ny in [(-dy,dx),(dy,-dx)]:
                if (xi+nx,yi+ny) in S and (xj+nx,yj+ny) in S:
                    cpt += 1
    return cpt//4

def main():
    N = int(input())
    P = [tuple(map(int,input().split())) for _ in range(N)]
    print(square_count(P))

main()
