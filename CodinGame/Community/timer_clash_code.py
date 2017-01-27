#!/usr/bin/env python3

p = 1
n = int(input())
start = 5*60
for _ in range(n):
    m,s = map(int,input().split(':'))
    t = 60*m+s
    if t<start and p>1:
        break
    start = max(0,t-256//(1<<(p-1)))
    p += 1
    if p==8:
        start = t

if p==1:
    print('NO GAME')
else:
    print('%d:%02d'%(start/60,start%60))
