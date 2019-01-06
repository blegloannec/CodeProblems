#!/usr/bin/env python3

import random
random.seed(42)

Case = [(5,100),(10,10**3),(20,10**6),(100,1<<32),(100,1<<60)]
for i in range(len(Case)):
    n,m = Case[i]
    for f in ['test','valid']:
        F = open('%s%d'%(f,i),'w')
        F.write('%d\n' % n)
        for _ in range(n):
            F.write('%d\n' % random.randint(5,m))
        F.close()
