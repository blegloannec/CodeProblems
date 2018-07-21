#!/usr/bin/env python

def problem17():
    L0_19 = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
    L10 = [0,0,6,6,5,5,5,7,6,6]
    c = 0
    for i in range(1,1000):
        k,l = i%100, i/100
        if k<20:
            c += L0_19[k]
        else:
            c += L10[k/10]+L0_19[k%10]
        if l>0 and k>0:
            c+=3
        if l>=1:
            c += L0_19[l]+7
    print c+11

problem17()
