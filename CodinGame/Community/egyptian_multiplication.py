#!/usr/bin/env python3

a,b = map(int,input().split())
if a<b:
    a,b = b,a

print('%d * %d' % (a,b))
B = ['']
ab = 0
while b:
    if b&1:
        ab += a
        B.append(str(a))
        b -= 1
    else:
        a <<= 1
        b >>= 1
    print('= %d * %d%s' % (a,b,' + '.join(B)))
print('= %d' % ab)
