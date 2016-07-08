#!/usr/bin/env python

import sys

# simple conversion
# romain -> entier -> romain optimal

C = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def rom2int(s):
    res = 0
    i = 0
    while i<len(s):
        if i+1<len(s) and C[s[i]]<C[s[i+1]]:
            res += C[s[i+1]]-C[s[i]]
            i += 2
        else:
            res += C[s[i]]
            i += 1
    return res

def int2rom(n):
    res = []
    while n>0:
        if n>=1000:
            res.append('M')
            n -= 1000
        elif n>=900:
            res.append('CM')
            n -= 900
        elif n>=500:
            res.append('D')
            n -= 500
        elif n>=400:
            res.append('CD')
            n -= 400
        elif n>=100:
            res.append('C')
            n -= 100
        elif n>=90:
            res.append('XC')
            n -= 90
        elif n>=50:
            res.append('L')
            n -= 50
        elif n>=40:
            res.append('XL')
            n -= 40
        elif n>=10:
            res.append('X')
            n -= 10
        elif n>=9:
            res.append('IX')
            n -= 9
        elif n>=5:
            res.append('V')
            n -= 5
        elif n>=4:
            res.append('IV')
            n -= 4
        else:
            res.append('I')
            n -= 1
    return ''.join(res)
        
def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        s = sys.stdin.readline().strip()
        print int2rom(rom2int(s))

main()
