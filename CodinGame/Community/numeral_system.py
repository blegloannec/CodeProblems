#!/usr/bin/env python3

L,R = input().split('=')
A,B = L.split('+')
b = 2
while True:
    try:
        if int(A,b)+int(B,b)==int(R,b):
            break
    except:
        pass
    b += 1
print(b)
