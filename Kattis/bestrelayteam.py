#!/usr/bin/env python3

N = int(input())
R = []
for _ in range(N):
    name,a,b = input().split()
    R.append((name, float(a), float(b)))
R.sort(key=(lambda nab: nab[2]))

b3 = sum(b for _,_,b in R[:3])
b4 = sum(b for _,_,b in R[:4])
tmin = float('inf')
for i, (name, a,b) in enumerate(R):
    if i<4: t = a + b4-b
    else:   t = a + b3
    if t<tmin:
        tmin = t; imin = i
print(tmin)
rmin = [R[imin][0]] + [name for i,(name,_,_) in enumerate(R[:4]) if i!=imin][:3]
print('\n'.join(rmin))
