#!/usr/bin/env python3

# ideal problem for a trie? let's use hashing then!
# actually we barely need it size the max size of things to hash is 7
HB = 29
HS = 7

num = lambda c: ord(c)-ord('a')+1

SYL = (5,7,5)
MAXSYL = max(SYL)+1  # bound on decomp size
def decomp(w, DP=None, i=0):
    if DP is None:
        DP = [None]*(len(w)+1)
        DP[len(w)] = 1
    if DP[i] is None:
        DP[i] = 0  # bitset of possible decomp. sizes
        h = 0
        for j in range(i, min(i+HS,len(w))):
            h = HB*h + num(w[j])
            if h in H:
                dpj = decomp(w, DP, j+1)
                DP[i] |= dpj<<1
    return DP[i]

def main():
    global H
    S = int(input())
    H = set()
    for _ in range(S):
        w = input()
        h = 0
        for c in w:
            h = HB*h + num(c)
        H.add(h)
    L = [input().split() for _ in range(len(SYL))]
    haiku = True
    for W, syl in zip(L, SYL):
        curr = 1
        for w in W:
            sw = decomp(w)
            curr0, curr = curr, 0
            for s in range(MAXSYL):
                if (sw>>s)&1:
                    curr |= curr0<<s
        if (curr>>syl)&1==0:
            haiku = False
            break
    print('haiku' if haiku else 'come back next year')

main()
