#!/usr/bin/env python3

for i in range(8):
    for j,p in enumerate(input().split()):
        if p=='K':
            ki,kj = i,j
        elif p!='_':
            ep = p
            ei,ej = i,j

if ep=='N':
    check = (abs(ki-ei),abs(kj-ej)) in ((1,2),(2,1))
else:
    check = (ep!='R' and abs(ki-ei)==abs(kj-ej)) or \
            (ep!='B' and (ki==ei or kj==ej))

print('Check' if check else 'No Check')
