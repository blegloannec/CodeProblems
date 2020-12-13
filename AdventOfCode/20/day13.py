#!/usr/bin/env python3

Tim = int(input())
Bus = [(i,int(x)) for i,x in enumerate(input().split(',')) if x!='x']


# Part 1
min_wait = float('inf')
for _,m in Bus:
    wait = (-Tim) % m
    if wait < min_wait:
        min_wait = wait
        part1 = m*wait
print(part1)


# Part 2
# NB: All given moduli are primes (hence pairwise coprime)
def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a//b)*v)

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

p,q = 0,1
for i,m in Bus:
    p = rev_chinois(p,q,-i,m)
    q *= m
print(p)
