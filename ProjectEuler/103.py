#!/usr/bin/env python

# NB a posteriori : pour le coup, ici (pour 7),
# la solution opti est en fait l'approx !

S6 = [11, 18, 19, 20, 22, 25]

def next_near(S):
    nS = [S[len(S)/2]]
    for i in xrange(len(S)):
        nS.append(nS[0]+S[i])
    return nS

def enum(n):
    i = 0
    s = []
    while n>0:
        if n&1:
            s.append(i)
        n >>= 1
        i += 1
    return s

def subsums(S):
    sums = []
    for s in xrange(1<<len(S)):
        ss = enum(s)
        sums.append((len(ss),sum(S[i] for i in ss)))
    return sums

def test(S):
    sums = subsums(S)
    for i in xrange(1,len(sums)):
        for j in xrange(i+1,len(sums)):
            if i&j==0:
                if sums[i][1]==sums[j][1]:
                    return False
                if sums[i][0]>sums[j][0] and sums[i][1]<sums[j][1]:
                    return False
                if sums[i][0]<sums[j][0] and sums[i][1]>sums[j][1]:
                    return False
    return True

# petites variations de S
def varia(S,R,i=0):
    if i==len(S):
        yield R
    else:
        for v in xrange(S[i]-2,S[i]+3):
            R[i] = v
            for U in varia(S,R,i+1):
                yield U

def main():
    nS7 = next_near(S6)
    s = 1000
    for R in varia(nS7,nS7[:]):
        if test(R):
            sR = sum(R)
            if sR<s:
                s = sR
                mins = ''.join(map(str,R))
    print mins

main()
