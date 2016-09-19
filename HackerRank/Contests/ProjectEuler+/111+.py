#!/usr/bin/env python

import sys

P10 = [10**n for n in xrange(41)]

def gen0(n,d,k,x,x0,n0,S):
    if k==0:
        if x>=x0 and x%2==1 and x%5!=0 and miller_rabin(x):
            S.append(x)
    else:
        if d==0 and n-1==n0: # for faster d=0 generation
            p = n0
            for e in xrange(int(p==n0),10):
                if e==d:
                    continue
                gen0(p,d,k-1,x+(e-d)*P10[p],x0,n0,S)
        else:
            for p in xrange(k-1,n):
                for e in xrange(int(p==n0),10):
                    if e==d:
                        continue
                    gen0(p,d,k-1,x+(e-d)*P10[p],x0,n0,S)

def gen(n,d,k):
    x = 0
    for i in xrange(n):
        x = 10*x+d
    x0 = 10**(n-1)
    S = []
    gen0(n,d,n-k,x,x0,n-1,S)
    return S

# Miller-Rabin deterministe 64 bits
def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def witness(a,n,b):
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n):
    b = digits(n-1,2)
    for w in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True

K = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 4, 4, 4, 4, 3, 3, 4, 4, 4], [4, 5, 4, 5, 5, 5, 5, 5, 5, 5], [5, 6, 5, 6, 5, 5, 5, 6, 5, 6], [6, 7, 7, 7, 6, 7, 7, 7, 7, 7], [7, 8, 8, 8, 8, 7, 8, 8, 8, 8], [8, 9, 8, 9, 9, 9, 9, 9, 8, 9], [9, 10, 10, 10, 10, 9, 10, 10, 9, 10], [10, 11, 10, 11, 11, 11, 10, 11, 11, 11], [11, 12, 11, 12, 11, 12, 11, 12, 11, 12], [12, 13, 13, 13, 12, 12, 12, 13, 13, 13], [12, 14, 14, 14, 13, 14, 13, 14, 14, 14], [14, 15, 14, 15, 14, 14, 14, 15, 14, 15], [15, 16, 15, 16, 15, 15, 15, 16, 16, 16], [16, 17, 17, 17, 16, 17, 17, 17, 16, 17], [17, 19, 17, 18, 17, 17, 17, 18, 18, 18], [18, 19, 18, 19, 19, 18, 19, 19, 18, 19], [19, 20, 19, 20, 19, 19, 20, 20, 19, 20], [20, 21, 20, 21, 20, 21, 21, 21, 20, 21], [21, 23, 21, 22, 21, 21, 22, 22, 21, 22], [21, 23, 22, 23, 22, 22, 22, 23, 22, 23], [23, 24, 23, 24, 23, 23, 23, 24, 23, 24], [24, 25, 24, 25, 25, 25, 24, 25, 24, 25], [25, 26, 25, 26, 25, 25, 25, 26, 25, 26], [26, 27, 27, 27, 27, 26, 27, 27, 26, 27], [27, 28, 27, 28, 27, 27, 27, 28, 27, 28], [28, 29, 28, 29, 29, 28, 28, 29, 28, 29], [28, 30, 29, 30, 29, 29, 29, 30, 29, 30], [30, 31, 30, 31, 31, 31, 30, 31, 30, 31], [30, 32, 31, 32, 31, 31, 31, 32, 31, 32], [31, 33, 32, 33, 32, 32, 32, 33, 32, 33], [32, 34, 33, 34, 33, 33, 33, 34, 34, 34], [34, 35, 35, 35, 34, 34, 34, 35, 34, 35], [35, 36, 35, 36, 35, 35, 35, 36, 35, 36], [36, 37, 36, 37, 36, 36, 36, 37, 36, 37], [37, 38, 37, 38, 37, 37, 37, 38, 37, 38], [38, 39, 38, 39, 38, 38, 38, 39, 38, 39]]

# Main
def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N,d = map(int,sys.stdin.readline().split())
        S = gen(N,d,K[N][d])
        S.sort()
        print ' '.join(map(str,S))

main()
