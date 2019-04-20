#!/usr/bin/env python3

import sys, os

S = 10000
Cases = [(2,1,1000), (3,1,1000), (5,2,2000), (1,3,3000), \
         (3,10,S), (5,15,S), (4,20,S), (2,25,S), (6,25,S), (1,30,S)]

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1] in ('clean','clear'):
        os.system('rm -f test* valid*')
    else:
        for i,(N,V,S) in enumerate(Cases):
            for Pref in ('test','valid'):
                base_name = '%s%d' % (Pref,i+1)
                os.system('python3 format_pgm.py --maxsize %d --shrink %d --out %s.pgm png/%s%d.png' % (S,V,base_name,Pref,N))
                #os.system('python3 solution.py < %s.pgm > %s_out.pgm' % (base_name,base_name))
                os.system('python3 solution.py < %s.pgm > %s_out' % (base_name,base_name))
