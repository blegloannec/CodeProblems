#!/usr/bin/env python3

def cost(S):
    c = 0
    for i in range(len(S)-1):
        if S[i]!=S[i+1]:
            c += X if S[i]=='C' else Y
    return c

def main():
    global X,Y
    T = int(input())
    for t in range(1, T+1):
        X,Y,S = input().split()
        X = int(X); Y = int(Y)
        res = 0
        if X>=0 and Y>=0:
            S = S.replace('?', '')
            res = cost(S)
        else:
            l = ''
            i = 0
            while i<len(S):
                k = 0
                while i<len(S) and S[i]=='?':
                    k += 1
                    i += 1
                r = S[i] if i<len(S) else ''
                # really not smart, but good enough...
                res += min(cost(l+'C'*k+r),
                           cost(l+'J'*k+r),
                           cost(l+('CJ'*((k+1)//2))[:k]+r),
                           cost(l+('JC'*((k+1)//2))[:k]+r))
                l = r
                i += 1
        print(f'Case #{t}: {res}')

main()
