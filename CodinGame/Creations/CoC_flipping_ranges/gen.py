#!/usr/bin/env python3

import random
random.seed(42)

Cases = [(10,5),(100,10),(1000,100),(10**5,500),(10**6,500)]

for T,(N,Q) in enumerate(Cases):
    for fname in ['test','valid']:
        F = open('%s%d'%(fname,T),'w')
        F.write('%d %d\n' % (N,Q))
        for _ in range(Q):
            L,R = random.randint(0,N-1),random.randint(0,N-1)
            if L>R:
                L,R = R,L
            F.write('%d %d\n' % (L,R))
        F.close()
