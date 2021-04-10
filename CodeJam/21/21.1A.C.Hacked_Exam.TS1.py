#!/usr/bin/env pypy

from fractions import gcd

def cnt1(x):
    o = 0
    while x:
        o += 1
        x &= x-1
    return o

def main():
    T = int(raw_input())
    for t in xrange(1, T+1):
        N,Q = map(int, raw_input().split())
        assert Q<30
        A = []; S = []
        for _ in xrange(N):
            a,s = raw_input().split()
            A.append(int(a[::-1].replace('T','1').replace('F','0'), 2))
            S.append(int(s))
        # brute-forcing solution candidates
        Sol = []
        for sol in xrange(1<<Q):
            valid = True
            for a,s in zip(A,S):
                diff = sol^a
                if cnt1(diff)!=Q-s:
                    valid = False
                    break
            if valid:
                Sol.append(sol)
        # building best answers
        C = len(Sol)
        Ans = []
        E = 0
        for i in xrange(Q):
            o = sum((sol>>i)&1 for sol in Sol)
            if 2*o>len(Sol):
                Ans.append('T')
                E += o
            else:
                Ans.append('F')
                E += C-o
        g = gcd(E, C)
        print('Case #{}: {} {}/{}'.format(t, ''.join(Ans), E/g, C/g))

main()
