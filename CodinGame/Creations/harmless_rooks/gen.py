#!/usr/bin/env python3

import random
random.seed(555)

N = [(5,0.25),(8,0.25),(16,0.25),(30,0.25),(50,0.3),(99,0.3),(99,0.4),(99,0.5)]

for i in range(len(N)):
    n,p = N[i]
    for fname in ['test','vali']:
        f = open(fname+str(i+1),'w')
        f.write(str(n)+'\n')
        for _ in range(n):
            f.write(''.join('X' if random.random()<p else '.' for _ in range(n))+'\n')
        f.close()
