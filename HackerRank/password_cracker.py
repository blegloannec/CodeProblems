#!/usr/bin/env python3

# similar to CG The Resistance
# could be optimized a lot, but good enough here

import sys
sys.setrecursionlimit(5000)

Memo = {}
def backtrack(i=0):
    if i==len(attempt):
        return True
    if i in Memo:
        return Memo[i] is not None
    for w in range(N):
        # of course the following test could be optimized, either:
        #    - using a trie for Passwd instead of a list
        # or - pre-computing all the starting positions of the words of Passwd
        #      in attempt (ideally using Aho-Corasick, or KMP or an std lib
        #      equivalent for each word as there is only few of them)
        # however the following is good enough as there are few (<=10) words
        # and they're small (<=10)
        if Passwd[w]==attempt[i:i+len(Passwd[w])]:
            if backtrack(i+len(Passwd[w])):
                Memo[i] = w
                return True
    Memo[i] = None
    return False

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        Passwd = input().split()
        attempt = input()
        Memo.clear()
        if backtrack():
            i = 0
            Sol = []
            while i<len(attempt):
                Sol.append(Passwd[Memo[i]])
                i += len(Sol[-1])
            print(' '.join(Sol))
        else:
            print('WRONG PASSWORD')
