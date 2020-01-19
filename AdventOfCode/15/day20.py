#!/usr/bin/env python

from math import sqrt

def diviseurs(n):
    if n==1:
        return [1]
    d = [1,n]
    s = int(sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            d.append(i)
            if n/i!=i:
                d.append(n/i)
    return d

def diviseurs2(n):
    if n==1:
        return [1]
    d = [1,n]
    s = int(sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            if n<=50*i:
                d.append(i)
            j = n/i
            if j!=i and n<=50*j:
                d.append(j)
    return d

def main():
    i = 1
    while sum(diviseurs(i))<3600000:
        i+=1
    print i

def main2():
    i = 1
    while 11*sum(diviseurs2(i))<36000000:
        i+=1
    print i  

main2()
