#!/usr/bin/env python3

import html

# Time || Problems list || Name || Info || Link || Code || Code ...
F = open('problems.txt','r').readlines()

def norm(s):
    return html.unescape(s.strip()).replace('&','&amp;')

def mark(ind,name,cont):
    print('  '*ind + '<%s>%s</%s>' % (name,norm(cont),name))

print('<?xml version="1.0" encoding="UTF-8"?>')
print('<?xml-stylesheet type="text/xsl" href="problems.xsl"?>')
print()
print('<problems>')
for L in F:
    L = L.replace('||','|').split('|')
    if len(L)<5:
        continue
    print('  <problem>')
    mark(2,'date',L[0])
    mark(2,'name',L[2])
    mark(2,'desc',L[3])
    mark(2,'link',L[4])
    P = L[1].split()
    for i in range(len(L)-5):
        print('    <ref>')
        mark(3,'num',P[i] if i<len(P) else '+')
        mark(3,'code',L[5+i])
        print('    </ref>')
    print('  </problem>')
print('</problems>')
