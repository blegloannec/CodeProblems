#!/usr/bin/env python3

import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

num = lambda c: ord(c)-ord('a')

P = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
MOD = 7389546599589289

def dp(l=0):
    if DP[l] is None:
        DP[l] = 0
        wl = S[l]
        h = 0
        for r in range(l,len(S)):
            wr = S[r]
            if h in H[wl][wr]:
                cnt = dp(r+1)
                if cnt>0:
                    DP[l] += H[wl][wr][h] * cnt
                    if DP[l]==1:
                        WordAt[l] = W[wl][wr][h]
            if r==l:
                h = 1
            else:
                h = (h*P[S[r]]) % MOD
    return DP[l]

def main():
    global S,H,W,DP,WordAt
    S = tuple(map(num, input().strip()))
    N = int(input())
    H = [[{} for _ in range(26)] for _ in range(26)]
    W = [[{} for _ in range(26)] for _ in range(26)]
    for _ in range(N):
        w = input().strip()
        w0 = num(w[0]); wf = num(w[-1])
        h = 1 if len(w)>1 else 0  # to distinguish 1/2-letter words
        for i in range(1,len(w)-1):
            h = (h*P[num(w[i])]) % MOD
        H[w0][wf][h] = H[w0][wf].get(h, 0) + 1
        W[w0][wf][h] = w
    DP = [None]*(len(S)+1)
    DP[-1] = 1
    WordAt = [None]*len(S)
    cnt = dp()
    if cnt==0:
        print('impossible')
    elif cnt>1:
        print('ambiguous')
    else:
        Sol = []
        i = 0
        while i<len(S):
            w = WordAt[i]
            Sol.append(w)
            i += len(w)
        print(' '.join(Sol))

main()
