#!/usr/bin/env pypy

# unfortunately fucked up this one during the contest...

from fractions import Fraction

def best_slope():
    Lower, Upper = Fraction(0), Fraction(1<<31,1)
    for i in xrange(N):
        Ci,Ji = CJ[i]
        for j in xrange(i+1,N):
            Cj,Jj = CJ[j]
            # we must have a*Ci + b*Ji < a*Cj + b*Jj
            # i.e. b(Ji-Jj) < a(Cj-Ci)
            # i.e. assuming Ji =/= Jj,
            #   either b/a < (Cj-Ci)/(Ji-Jj)  if Ji>Jj
            #   or     b/a > (Cj-Ci)/(Ji-Jj)  otherwise
            if Ci==Cj:
                if Ji>=Jj:
                    return None
            elif Ji==Jj:
                if Ci>=Cj:
                    return None
            elif Ji>Jj:
                Upper = min(Upper, Fraction(Cj-Ci,Ji-Jj))
            else:
                Lower = max(Lower, Fraction(Cj-Ci,Ji-Jj))
    if Upper<=Lower:
        return None
    # we have the bounds, let us compute the
    # min pair (a,b) such that Lower < b/a < Upper
    # we first use a dicho search to find the smallest
    # acceptable denominator a
    M = (Lower + Upper) * Fraction(1,2)
    ql, qr = 1, 1<<62
    while ql<qr:
        q = (ql+qr)/2
        # we check whether there exists q0 <= q such that
        # there exists p0 such that Lower < p0/q0 < Upper
        # /!\ that does NOT imply that there exists
        #     p such that Lower < p/q < Upper
        #    (that's why you need an approximation technique
        #     such as limit_denominator() here)
        if Lower < M.limit_denominator(q) < Upper:
            qr = q
        else:
            ql = q+1
    a = ql
    b = int(a*Lower + 1)
    return (a,b)

if __name__=='__main__':
    T = int(raw_input())
    for t in xrange(1,T+1):
        N = int(raw_input())
        CJ = [tuple(map(int,raw_input().split())) for _ in xrange(N)]
        S = best_slope()
        if S is None:
            print 'Case #%d: IMPOSSIBLE' % t
        else:
            print 'Case #%d: %d %d' % (t,S[0],S[1])
