#!/usr/bin/env python3

from operator import *

M = (1<<8)-1

def emul(P):
    AOp = [add,sub]
    BOp = [or_,and_,xor]
    COp = [eq,ne]
    R = [0]*3
    i = 0
    while i<len(P):
        O = P[i:i+4]
        C = int(O[0],16)
        if C==0:
            break
        elif C==1:
            k = int(O[1],16)
            n = int(O[2:],16)
            R[k] = n
        elif C<=3:
            x = int(O[2],16)
            y = int(O[3],16)
            v = AOp[C-2](R[x],R[y])
            R[x] = v&M
            R[2] = int(not 0<=v<=M)
        elif C<=6:
            x = int(O[2],16)
            y = int(O[3],16)
            R[x] = BOp[C-4](R[x],R[y])
        elif C<=8:
            k = int(O[1],16)
            n = int(O[2:],16)
            if COp[C-7](R[k],n):
                i += 4
        else:
            x = int(O[2],16)
            y = int(O[3],16)
            if COp[C-9](R[x],R[y]):
                i += 4
        i += 4
    return R

print(*emul(input()))
