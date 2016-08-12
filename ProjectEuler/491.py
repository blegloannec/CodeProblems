#!/usr/bin/env python

# 10^n = (-1)^n mod 11
# un nb est divisible par 11
# si la difference entre la somme des chiffres
# en position paire et celle des chiffres en
# position impaire est divisible par 11

def parmi(n,p):
    if p==0:
        yield []
    else:
        for i in xrange(p/2,n):
            for S in parmi(i,p-1):
                S.append((i,1))
                yield S
        if p>1:
            for i in xrange((p-1)/2,n):
                for S in parmi(i,p-2):
                    S.append((i,2))
                    yield S

# 8! = 40320
# 9! = 362880
# 10! = 3628800

def main():
    cpt = 0
    for S in parmi(10,10):
        C = [0 for _ in xrange(10)]
        s = 0
        for (x,m) in S:
            s += x*m
            C[x] = m
        d = 1
        for i in xrange(10):
            if C[i]==0 or C[i]==2:
                d *= 2
        if (s-(90-s))%11==0:
            if C[0]==2:
                c = 9*8*40320
            elif C[0]==1:
                c = 9*362880
            else:
                c = 3628800
            cpt += (c*3628800)/d
    print cpt

main()
