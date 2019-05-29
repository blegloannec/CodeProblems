#!/usr/bin/env python3

# counting words of size N over an alphabet of size M
# that do not contain any factor of the form "aa" or "aba"
#  - initialize by picking 2 distinct letters: M(M-1) choices
#  - successively append N-2 letters at the end by picking each
#    time a letter distinct from the last two:
#    (M-2) choices per letter, (M-2)^(N-2) in total

P = 10**9+7

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    if N==1:
        res = M
    else:
        res = (M * (M-1) * pow(M-2,N-2,P)) % P
    print(res)
