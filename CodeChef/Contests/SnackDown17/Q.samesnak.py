#!/usr/bin/env python3

def same(XA1,YA1,XA2,YA2,XB1,YB1,XB2,YB2):
    if (XA1==XA2==XB1==XB2) or (YA1==YA2==YB1==YB2):
        if YA1==YA2==YB1==YB2:
            YA1,YA2,YB1,YB2 = XA1,XA2,XB1,XB2
        if YA1>YA2:
            YA1,YA2 = YA2,YA1
        if YB1>YB2:
            YB1,YB2 = YB2,YB1
        return max(YA1,YB1)<=min(YA2,YB2)
    # cas orthogonal ou // disjoint
    return (XA1,YA1)==(XB1,YB1) or (XA1,YA1)==(XB2,YB2) or (XA2,YA2)==(XB1,YB1) or (XA2,YA2)==(XB2,YB2)

def main():
    T = int(input())
    for _ in range(T):
        XA1,YA1,XA2,YA2 = map(int,input().split())
        XB1,YB1,XB2,YB2 = map(int,input().split())
        print('yes' if same(XA1,YA1,XA2,YA2,XB1,YB1,XB2,YB2) else 'no')

main()
