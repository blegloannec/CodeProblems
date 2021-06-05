#!/usr/bin/env python3

def looknsay_rev(S):
    if len(S)&1:
        return None
    R = []
    for i in range(0,len(S),2):
        if S[i]==0 or (i>0 and S[i+1]==S[i-1]):
            return None
        R += [S[i+1]]*S[i]
    return R

def main():
    S = list(map(int,input()))
    R = looknsay_rev(S)
    while R!=None and R!=S:
        S,R = R,looknsay_rev(R)
    print(''.join(map(str,S)))

main()
