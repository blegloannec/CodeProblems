#!/usr/bin/env python
import sys
l = open(sys.argv[1],'r').readlines()
for i in range(1,int(l[0])+1):
    print 'Case #%d: %s' % (i,' '.join(l[i].split()[::-1]))
