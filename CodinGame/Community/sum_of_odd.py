#!/usr/bin/env python3

# sum( 2*k+1, k=a..a+l-1 ) = (2a+l)*l

n = int(input())

cnt = lmax = 0
l = 2
while l*l<=n:
    if n%l==0:
        dapl = n//l
        if dapl>=l and (dapl-l)%2==0:
            cnt += 1
            if l>lmax:
                lmax = l
                amax = (dapl-l)//2
    l += 1

print(cnt)
if cnt>0:
    print(2*amax+1,2*(amax+lmax-1)+1)
