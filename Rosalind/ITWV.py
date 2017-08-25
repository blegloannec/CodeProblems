#!/usr/bin/env python3

import sys

memo = {}
# S,A,B les trois chaines globales
# dp(s,a,b) = vrai ssi on peut entrelacer A[:a] et B[:b] dans S[:s]
#             jusqu'a la position s-1 exactement
def dp(s,a,b):
    if (s,a,b) in memo:
        return memo[s,a,b]
    if a==b==0:
        return True
    if s==0:
        return False
    res = (a>0 and S[s-1]==A[a-1] and dp(s-1,a-1,b)) or (b>0 and S[s-1]==B[b-1] and dp(s-1,a,b-1))
    memo[s,a,b] = res
    return res

def interweave(s,t,u):
    global S,A,B
    S,A,B = s,t,u
    memo.clear()
    return any(dp(i,len(A),len(B)) for i in range(1,len(S)+1))

def main():
    L = sys.stdin.readlines()
    s = L[0].strip()
    DNAS = [A.strip() for A in L[1:]]
    for t in DNAS:
        L = []
        for u in DNAS:
            L.append(str(int(interweave(s,t,u))))
        print(' '.join(L))

main()
