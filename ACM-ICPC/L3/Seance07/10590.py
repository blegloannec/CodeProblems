#!/usr/bin/env python3

import sys

M = 5001
P = [0]*M

# calcul en O(m*sqrt(m)) via formule d'Euler pour les partitions
# (voir aussi HR PE+ 78)
def precomp():
    P[0] = P[1] = 1
    for n in range(2,M):
        k = 1
        while k*(3*k-1)//2<=n:
            if k*(3*k+1)//2<=n:
                P[n] += (1 if (k+1)%2==0 else -1)*(P[n-k*(3*k+1)//2]+P[n-k*(3*k-1)//2])
            else:
                P[n] += (1 if (k+1)%2==0 else -1)*P[n-k*(3*k-1)//2]
            k += 1

def main():
    precomp()
    for L in sys.stdin.readlines():
        N = int(L)
        print(P[N])

main()
