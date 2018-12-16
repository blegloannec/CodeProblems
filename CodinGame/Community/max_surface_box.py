#!/usr/bin/env python3

# "naive" solution, without even caring about factoring N

N = int(input())
mini,maxi = float('inf'),0
for x in range(1,int(N**(1/3))+2):
    if N%x==0:
        M = N//x
        for y in range(x,int(M**(1/2))+1):
            if M%y==0:
                z = M//y
                a = 2*(x*y+x*z+y*z)
                mini = min(mini,a)
                maxi = max(maxi,a)
print(mini,maxi)
