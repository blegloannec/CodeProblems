#!/usr/bin/env python3

n = int(input())
s = 0
for _ in range(n):
    si,di = map(int,input().split())
    # si + k*di >= s
    # k >= (s-si)/di
    k = max(0,(s-si+di-1)//di)
    s = si+k*di+1
print(s-1)
