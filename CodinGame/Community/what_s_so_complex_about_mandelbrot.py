#!/usr/bin/env python3

# worthless puzzle, mostly to use python complex type for once
# abs(c) gives the magnitude (module) of complex c

c = complex(input().replace('i','j'))
m = int(input())

i = x = 0
while i<m and abs(x)<=2:
    x = x*x+c
    i += 1
print(i)
