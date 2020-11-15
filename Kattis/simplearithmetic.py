#!/usr/bin/env python3

a,b,c = map(int, input().split())
e,a = divmod(a*b, c)
F = []
for _ in range(6):
    d,a = divmod(10*a, c)
    F.append(str(d))
print(f'{e}.{"".join(F)}')
