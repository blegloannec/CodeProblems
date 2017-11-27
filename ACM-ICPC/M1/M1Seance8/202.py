#!/usr/bin/env python3

import sys

def main():
    for L in sys.stdin.readlines():
        p,q = map(int,L.split())
        seen = [-1]*q
        E = p//q
        r = p-E*q
        D = []
        while seen[r]<0:
            seen[r] = len(D)
            a,r = divmod(10*r,q)
            D.append(a)
        t = seen[r]
        pre = ''.join(map(str,D[:t]))
        per = ''.join(map(str,D[t:]))
        if len(pre)+len(per)>50:
            per = per[:50-len(pre)]+'...'
        print('%d/%d = %d.%s(%s)' % (p,q,E,pre,per))
        print('   %d = number of digits in repeating cycle' % (len(D)-t))
        print()

main()
