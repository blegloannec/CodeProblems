#!/usr/bin/env python3

def prime(p):
    if p<3:
        return p==2
    if p%2==0:
        return False
    d = 3
    while d*d<=p:
        if p%d==0:
            return False
        d += 2
    return True

def main():
    while True:
        p,a = map(int,input().split())
        if p==0:
            break
        print('yes' if pow(a,p,p)==a and not prime(p) else 'no')

main()
