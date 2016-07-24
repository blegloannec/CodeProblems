#!/usr/bin/env python

simp = range(1,21)
trip = [3*i for i in simp]
simp.append(25)
doub = [2*i for i in simp]
tout = sorted(simp+doub+trip)

# compte tenu de la profondeur, on ne memoise meme pas...

def DP(n,k=3,d=True,tmax=None):
    if k==0:
        return 1 if n==0 else 0
    if n==0:
        return 1
    res = 0
    if d:
        for v in doub:
            if v>n:
                break
            res += DP(n-v,k-1,False,len(tout)-1)
    else:
        for i in xrange(tmax+1):
            if tout[i]>n:
                break
            res += DP(n-tout[i],k-1,False,i)
    return res

print sum(DP(i) for i in xrange(1,100))
