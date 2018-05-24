#!/usr/bin/env python3

from math import log

EMAX = 54

def dicho(a,x):
    l,r = 0,EMAX
    while l<r:
        m = (l+r)//2
        if pow(a,m,x)==0:
            r = m
        else:
            l = m+1
    return l

def limit(a,x):
    if pow(a,EMAX,x)!=0:
        return -1
    return dicho(a,x)

# A[i]^A[i+1]^...^A[j] >= x
def suptower(i,j,x):
    if i>j:
        return 1>=x
    if A[i]<=1:
        return A[i]>=x
    if A[i]>=x and (i==j or A[i+1]>0):
        return True
    # A[i]^y >=x, y >= log(x,A[i])
    return suptower(i+1,j,log(x,A[i]))

def find(i,j,x):
    if x==1:
        return True
    y = limit(A[i],x)
    if y<0:
        return False
    return suptower(i+1,j,y)

def main():
    global A
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    for _ in range(Q):
        i,j,x = map(int,input().split())
        print('Yes' if find(i-1,j-1,x) else 'No')

main()
