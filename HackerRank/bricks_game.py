#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        # reversed because given "from top to bottom"
        B = list(map(int,reversed(input().split())))
        SB = B[:]  # sommes prefixes
        for i in range(1,N):
            SB[i] += SB[i-1]
        # Prog. Dyn. (pourrait etre implementee en espace O(1))
        O = SB[:]  
        for i in range(3,N):
            O[i] = max(SB[i]-O[i-k] for k in range(1,4))
        print(O[N-1])

main()
