#!/usr/bin/env python

import re

re1 = re.compile('|'.join([chr(i)+chr(i+1)+chr(i+2) for i in range(97,121)]))
re2 = re.compile('[iol]')
re3 = re.compile(r'(.)\1.*(.)\2')

def c1(s):
    return (re1.search(s)!=None)

def c2(s):
    return (re2.search(s)==None)

def c3(s):
    return (re3.search(s)!=None)

def inc(s):
    i = len(s)-1
    l = []
    while s[i]=='z':
        l.append('a')
        i -= 1
    if i<0:
        l.append('a')
        return ''.join(l[::-1])
    l.append(chr(ord(s[i])+1))
    return s[:i]+''.join(l[::-1])

def main():
    #s = inc('hxbxwxba')
    s = inc('hxbxxyzz')
    while not (c1(s) and c2(s) and c3(s)):
        s = inc(s)
    print s


main()
