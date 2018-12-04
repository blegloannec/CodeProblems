#!/usr/bin/env python3

def is_prime(n):
    if n<=2:
        return n==2
    if n&1==0:
        return False
    d = 3
    while d*d<=n:
        if n%d==0:
            return False
        d += 2
    return True

def horiz(R,C,Gfun):  # O(R*C^2)
    P = set()
    for i in range(R):
        for l in range(C):
            x = 0
            for r in range(l,C):
                x = 10*x + Gfun(i,r)
                if is_prime(x):
                    P.add(x)
    return P

def main():
    R,C = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(R)]
    P = horiz(R,C,(lambda i,j: G[i][j])) | horiz(C,R,(lambda j,i: G[i][j]))
    print(len(P))

main()
