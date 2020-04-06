#!/usr/bin/env python3

# lazy implementation (we recompute the position and score each turn)
# but way good enough

def last_CS(P):
    for i in range(len(P)-2,-1,-1):
        if (P[i],P[i+1])==('C','S'):
            return i
    return None

def eval(P):
    s = 1
    res = 0
    for c in P:
        if c=='C':
            s *= 2
        else:
            res += s
    return res

def main():
    T = int(input())
    for cas in range(1,T+1):
        D,P = input().split()
        D = int(D)
        P = list(P)
        S = eval(P)
        i = last_CS(P)
        res = 0
        while S>D and i!=None:
            P[i],P[i+1] = P[i+1],P[i]
            res += 1
            S = eval(P)
            i = last_CS(P)
        if S>D:
            print('Case #%d: IMPOSSIBLE' % cas)
        else:
            print('Case #%d: %d' % (cas,res))

main()
