#!/usr/bin/env pypy

import sys

def main():
    T = int(sys.stdin.readline())
    for t in xrange(1,T+1):
        L,R = map(int,sys.stdin.readline().split())
        K = 1
        while L>=K or R>=K:
            swap = False
            if L<R:
                L,R = R,L
                swap = True
            D = L-R
            if D>=K:
                a,b = 1, 1<<30
                while a<b:
                    m = (a+b+1)//2
                    sk = m*K + m*(m-1)//2
                    if D>=sk:
                        a = m
                    else:
                        b = m-1
                L -= a*K + a*(a-1)//2
                K += a
            elif L>=K and R>=K+1:
                a,b = 1, 1<<30
                while a<b:
                    m = (a+b+1)//2
                    l = L - (K*m + m*(m-1))
                    r = R - (K*m + m*m)
                    if l>=r>=0:
                        a = m
                    else:
                        b = m-1
                L -= K*a + a*(a-1)
                R -= K*a + a*a
                K += 2*a
            else:
                L -= K
                K += 1
            if swap:
                L,R = R,L
        K -= 1
        sys.stdout.write('Case #%d: %d %d %d\n' % (t,K,L,R))

main()
