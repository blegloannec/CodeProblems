#!/usr/bin/env python

import sys

def c2i(c):
    return ord(c)-ord('A')

def sig(s):
    res = [0 for _ in xrange(26)]
    for c in s:
        res[c2i(c)] += 1
    return res

def decr(s1,s2):
    for i in xrange(26):
        s2[i] -= s1[i]



data = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
sigs = [sig(d) for d in data]

def main():
    global res
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        S = sys.stdin.readline().strip()
        s = sig(S)
        res = []
        while s[c2i('Z')]>0:
            res.append(0)
            decr(sigs[0],s)
        while s[c2i('U')]>0:
            res.append(4)
            decr(sigs[4],s)
        while s[c2i('W')]>0:
            res.append(2)
            decr(sigs[2],s)
        while s[c2i('X')]>0:
            res.append(6)
            decr(sigs[6],s)
        while s[c2i('F')]>0:
            res.append(5)
            decr(sigs[5],s)
        while s[c2i('O')]>0:
            res.append(1)
            decr(sigs[1],s)
        while s[c2i('V')]>0:
            res.append(7)
            decr(sigs[7],s)
        while s[c2i('N')]>0:
            res.append(9)
            decr(sigs[9],s)
        while s[c2i('I')]>0:
            res.append(8)
            decr(sigs[8],s)
        while s[c2i('H')]>0:
            res.append(3)
            decr(sigs[3],s)
        print 'Case #%d: %s' % (t,''.join(map(str,sorted(res))))

main()
