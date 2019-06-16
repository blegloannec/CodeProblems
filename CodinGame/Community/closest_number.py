#!/usr/bin/env python3

# See also CodeJam 2016 1B.B Close Match

# O(N) approach
def closest(N,M):
    Size = len(M)
    CntM = [0]*10
    for c in M:
        CntM[int(c)] += 1
    if Size<len(N):  # simple corner case
        return ''.join(str(i)*CntM[i] for i in range(9,-1,-1))
    IntN = int(N)
    N = '0'*(Size-len(N)) + N
    # equalizing N as much as possible from left to right
    i = 0
    while i<Size and CntM[int(N[i])]>0:
        CntM[int(N[i])] -= 1
        i += 1
    if i==Size:
        return N
    # moving backwards to find the best inf and sup candidates
    best_diff = float('inf')
    sup_req = inf_req = True
    while i>=0 and (inf_req or sup_req):
        if inf_req:
            try:
                c = next(c for c in range(int(N[i])-1,-1,-1) if CntM[c]>0)
                CntM[c] -= 1
                cand = int(N[:i] + str(c) + ''.join(str(i)*CntM[i] for i in range(9,-1,-1)))
                diff = IntN - cand
                if diff<=best_diff:
                    best_diff, best = diff, cand
                CntM[c] += 1
                inf_req = False
            except StopIteration:
                pass
        if sup_req:
            try:
                c = next(c for c in range(int(N[i])+1,10) if CntM[c]>0)
                CntM[c] -= 1
                cand = int(N[:i] + str(c) + ''.join(str(i)*CntM[i] for i in range(10)))
                diff = cand - IntN
                if diff<best_diff:
                    best_diff, best = diff, cand
                CntM[c] += 1
                sup_req = False
            except StopIteration:
                pass
        i -= 1
        if i>=0:
            CntM[int(N[i])] += 1
    return str(best)

if __name__=='__main__':
    N,M = input().split()
    print(closest(N,M))
