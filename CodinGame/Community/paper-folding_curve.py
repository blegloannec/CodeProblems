#!/usr/bin/env python3

# classic https://en.wikipedia.org/wiki/Dragon_curve

_ = int(input())
l,r = map(int,input().split())

print(''.join('0' if ((i&-i)<<1)&i else '1' for i in range(l+1,r+2)))
