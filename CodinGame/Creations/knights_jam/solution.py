#!/usr/bin/env python3

# Possible approaches:
#  - standard BFS (naive)
#  - cycle through the configurations space by local swaps
#  - explicit formula (below)

def dist(C):
    if C[4]!='5':
        return -1
    P = (0,5,6,1,8,3,2,7)
    S = [C[i] for i in P]
    i0 = S.index('.')
    S.pop(i0)
    i1 = S.index('1')
    if ''.join(S[i1:]+S[:i1])!='1672438':
        return -1
    if i1==0:
        return abs(i0-4)
    left  =   i0 + (6-i1)*8 + 4
    right = 7-i0 + (i1-1)*8 + 5
    return min(left,right)

print(dist(''.join(input() for _ in range(3))))
