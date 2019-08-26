#!/usr/bin/env python3

import random, sys, os
random.seed(7531)

Cases = ((10,10),(10,20),(5,100),(7,500),(5,1000),(3,2000))

def make_file(fname, I):
    F = open(fname, 'w')
    F.write('%d\n' % len(I))
    for xy in I:
        F.write('%d %d\n' % xy)
    F.close()

def gen_case(t, T, L):
    Itest, Ivalid = ([(2*random.randint(1,L//2),2*random.randint(1,L//2)) for _ in range(T)] for _ in range(2))
    make_file('test%d'%t, Itest)
    make_file('valid%d'%t, Ivalid)

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1] in ('clear','clean'):
        os.system('rm -f test* valid*')
    else:
        for i,(T,L) in enumerate(Cases):
            gen_case(i+2,T,L)
