#!/usr/bin/env python

def pandigital(m,n,k):
    t = [False for _ in xrange(k+1)]
    t[0] = True
    cpt = 0
    r = []
    for i in xrange(1,n+1):
        mi = m*i
        r.append(str(mi))
        while mi>0:
            c = mi%10
            if c>k or t[c]:
                return (False,0)
            t[c] = True
            cpt += 1
            mi /= 10
    return (cpt==k, int(''.join(r)))

def main():
    res = 0
    for m in xrange(2,10000):
        for n in xrange(2,10):
            b,r = pandigital(m,n,9)
            if b and r>res:
                res = r
    print res

main()
