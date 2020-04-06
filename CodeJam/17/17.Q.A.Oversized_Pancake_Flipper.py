#!/usr/bin/env python3

# O(SK) greedy
def solve(S,K):
    cpt = 0
    for i in range(len(S)-K+1):
        if not S[i]:
            for j in range(i,i+K):
                S[j] = not S[j]
            cpt += 1
    if all(S[-K+1:]):
        return cpt
    else:
        return -1

def main():
    T = int(input())
    for t in range(1,T+1):
        S,K = input().split()
        S = [s=='+' for s in S]
        K = int(K)
        res = solve(S,K)
        print('Case #%d: %s' % (t,str(res) if res>=0 else 'IMPOSSIBLE'))

main()
