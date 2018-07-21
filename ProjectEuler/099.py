#!/usr/bin/python

from math import log

maxlog = 0
line = 1
f = open('input/99_base_exp.txt','r')

for l in f.readlines():
    s = l.split(',')
    a = int(s[0])
    b = int(s[1])
    mylog = b*log(a)
    if mylog>maxlog:
        maxlog = mylog
        maxline = line
    line += 1
        
print maxline
