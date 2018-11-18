#!/usr/bin/env python3

def val(l,i,j):
    if l==0:
        return '0'
    s = 3**(l-1)
    if s<=i<2*s and s<=j<2*s:
        return '+'
    return val(l-1,i%s,j%s)

def main():
    L = int(input())
    y1,x1,y2,x2 = map(int,input().split())
    for i in range(x1,x2+1):
        print(''.join(val(L,i,j) for j in range(y1,y2+1)))

main()
