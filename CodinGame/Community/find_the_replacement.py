#!/usr/bin/env python3

X = input()
Y = input()
if X==Y:
    print('NONE')
else:
    R = {}
    O = []
    for x,y in zip(X,Y):
        if x not in R:
            R[x] = y
            O.append(x)
        elif y!=R[x]:
            R = None
            break
    if R is None:
        print("CAN'T")
    else:
        for x in O:
            if x!=R[x]:
                print('%s->%s' % (x,R[x]))
