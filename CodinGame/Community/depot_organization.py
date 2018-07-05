#!/usr/bin/env python3

from collections import defaultdict

T = []
D = defaultdict(list)
D0 = defaultdict(list)

def rot(t,i=1):
    return tuple(t[i:]+t[:i])

I = [None]*7
S = [None]*7
def backtrack(i=0,used=0):
    if i==0:  # center
        for k in range(7):
            I[0],S[0] = k,T[k]
            if backtrack(1,1<<k):
                return True
    elif i==1:  # right of center
        for k,t in D0[S[0][0]]:
            if used&(1<<k)==0:
                I[1],S[1] = k,t
                if backtrack(2,used|(1<<k)):
                    return True
    elif i==7:  # closing the loop
        return S[1][2]==S[6][5]
    else:  # counter-clockwise ordering from top-right of center to bottom right of center
        p = S[i-1][(-i)%6],S[0][7-i]  # pair of common colors with previous cell and center
        for k,t in D[p]:
            if used&(1<<k)==0:
                I[i],S[i] = k,rot(t,(3+i)%6)
                if backtrack(i+1,used|(1<<k)):
                    return True
    return False

def main():
    for i in range(7):
        t = tuple(input().split())
        m = min(t)
        for _ in range(6):
            if t[0]==m:
                T.append(t)
            D0[t[3]].append((i,t))
            D[tuple(t[:2])].append((i,t))
            t = rot(t)
    backtrack()
    print(' '.join(str(I[i])+S[i][0] for i in [3,2,4,0,1,5,6]))

main()
