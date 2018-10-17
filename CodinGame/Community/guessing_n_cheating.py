#!/usr/bin/env python3

R = int(input())
l,r = 1,100
cheat = False
for i in range(R):
    x,_,answer = input().split()
    x = int(x)
    if answer=='high':
        r = min(r,x-1)
    elif answer=='low':
        l = max(l,x+1)
    if l>r or (answer=='on' and not l<=x<=r):
        cheat = True
        break
if cheat:
    print('Alice cheated in round',i+1)
else:
    print('No evidence of cheating')
