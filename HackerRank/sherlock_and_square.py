#!/usr/bin/env python3

# square_count(N) = 4^N
# square_size(N) = 1/2^N
# length(N) = length(N-1) + square_count(N-1)*2*square_size(N-1)
#           = length(N-1) + 2^N
#           = 4 + sum(2^i, i=1..N)
#           = 4 + (2^(N+1)-2)/(2-1)
#           = 2 + 2^(N+1)

P = 10**9+7

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print((2+pow(2,N+1,P)) % P)

main()
