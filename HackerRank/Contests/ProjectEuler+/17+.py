#!/usr/bin/env python

import sys

def num2words(n,force=False):
    L0_19 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    L10 = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    if n>=1000000000:
        return num2words(n/1000000000)+['Billion']+num2words(n%1000000000)
    if n>=1000000:
        return num2words(n/1000000)+['Million']+num2words(n%1000000)
    if n>=1000:
        return num2words(n/1000)+['Thousand']+num2words(n%1000)
    if n>=100:
        return [L0_19[n/100],'Hundred']+num2words(n%100)
    if n>=20:
        return [L10[n/10]]+num2words(n%10)
    if n>0 or (n==0 and force):
        return [L0_19[n]]
    return []

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        print ' '.join(num2words(N,True))

main()
