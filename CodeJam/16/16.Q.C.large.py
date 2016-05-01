#!/usr/bin/env python

import sys,random
random.seed()

def decomp2(n):
    res = []
    while n>0:
        res.append(n%2)
        n/=2
    return res

def witness(a,n):
    b = decomp2(n-1)
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n,s):
    for j in xrange(s):
        if witness(random.randint(1,n-1),n):
            return False
    return True

def convert(n,b):
    res = 0
    for c in n:
        res = b*res+c
    return res

def first_div(n,cmax):
    if n%2==0:
        return (True,2)
    i = 3
    while i<cmax:
        if n%i==0:
            return (True,i)
        i += 2
    return (False,0)
        

def main():
    print 'Case #1:'
    s = set()
    while len(s)<500:
        n = random.randint((1<<31)+1,(1<<32)-1)
        #n = random.randint((1<<5)+1,(1<<6)-1)
        if n%2==0 or (n in s):
            continue
        dn = decomp2(n)[::-1]
        jam = True
        for b in xrange(2,11):
            if miller_rabin(convert(dn,b),30):
                jam = False
                break
        if jam:
            facile = True
            D = []
            for b in xrange(2,11):
                trouv,divi = first_div(convert(dn,b),1000)
                if not trouv:
                    facile = False
                    break
                D.append(divi)
            if facile:
                s.add(n)
                print '%s %s' % (''.join(map(str,dn)),' '.join(map(str,D)))

main()
