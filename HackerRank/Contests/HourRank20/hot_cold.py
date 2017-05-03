#!/usr/bin/env python3

c1,c2,h1,h2 = map(int,input().split())
print('YES' if max(c1,c2)<=min(h1,h2) else 'NO')
