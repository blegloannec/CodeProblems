#!/usr/bin/env python

import sys

def valid(curr,req):
    for i in xrange(26):
        if curr[i]<req[i]:
            return False
    return True

def main():
    S = map((lambda x: ord(x)-ord('a')),sys.stdin.readline().strip())[::-1]
    cpt = [0 for i in xrange(26)]
    for c in S:
        cpt[c] += 1
    req = map((lambda x: x/2),cpt)
    req_size = sum(req)
    pos = 0
    sol = []
    curr = cpt[:]
    while len(sol)<req_size:
        best_pos = None
        for i in xrange(pos,len(S)):
            if not valid(curr,req):
                break
            if req[S[i]]>0 and (best_pos==None or S[i]<S[best_pos]):
                best_pos = i
                best_curr = curr[:]
            curr[S[i]] -= 1
        pos = best_pos+1
        sol.append(S[best_pos])
        curr = best_curr
        curr[S[best_pos]] -= 1
        req[S[best_pos]] -= 1
    print ''.join(map((lambda x: chr(x+ord('a'))),sol))

main()
