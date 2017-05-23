#!/usr/bin/env python3

def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    xc,yc = map(int,input().split())
    dx = min(xc-x1,x2-xc)
    dy = min(yc-y1,y2-yc)
    print(((2*dx+1)*(2*dy+1)-1)//2)

main()
