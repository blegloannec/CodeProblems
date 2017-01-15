#!/usr/bin/env python

import sys

# 7 premier avec 4 engendre Z/4Z
# donc pour tout n il existe 0<=k<=3 tel que n = k*7 mod 4
# plus precisement 7^(-1) = 3 mod 4 donc k = (3*n)%4
# si n >= 3*7, alors n >= k*7 et n-k*7 >= 0 est multiple de 4
# et plus precisement n lucky ssi n >= ((3*n)%4)*7

q = int(sys.stdin.readline())
for _ in xrange(q):
    n = int(sys.stdin.readline())
    print 'Yes' if n>=((3*n)%4)*7 else 'No'
