#!/usr/bin/env python

import sys

INV = {'0':'1','1':'0'}

def assoc(d,O,D):
    res = None
    for o in O:
        # charger d sur o
        h = 0
        v = []
        for i in xrange(len(d)):
            if d[i]!=o[i]:
                v.append(True)
                h += 1
            else:
                v.append(False)
        valid = True
        for p in O:
            q = ''.join([INV[p[i]] if v[i] else p[i] for i in xrange(len(p))])
            # par hyp les q sont distincts
            if not (q in D):
                valid = False
                break
        if valid:
            res = min(res,h) if res!=None else h
    return res

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N,L = map(int,sys.stdin.readline().split())
        O = sys.stdin.readline().split()
        D = sys.stdin.readline().split()
        d = D[0]
        D = set(D)
        res = assoc(d,O,D)
        if res==None:
            print 'Case #%d: NOT POSSIBLE' % (t)
        else:
            print 'Case #%d: %d' % (t,assoc(d,O,D))

main()
