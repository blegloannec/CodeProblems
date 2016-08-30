#!/usr/bin/env python

# Backtracking (on the successive digits, updating the correct guesses
# vector all along) + meet-in-the-middle (memorize a solution for each
# correct guesses vector for the first half and find a complementary
# solution for the second half)

## Data
#K,V = 5,10
#G = ['90342','70794','39458','34109','51545','12531']
#C0 = [2,0,2,1,2,1]

K,V = 16,10
G = ['5616185650518293','3847439647293047','5855462940810587','9742855507068353','4296849643607543','3174248439465858','4513559094146117','7890971548908067','8157356344118483','2615250744386899','8690095851526254','6375711915077050','6913859173121360','6442889055042768','2321386104303845','2326509471271448','5251583379644322','1748270476758276','4895722652190306','3041631117224635','1841236454324589','2659862637316867']
C0 = [2,1,3,3,3,1,2,3,1,2,3,1,1,2,0,2,2,3,1,3,3,2]

## Aux
def getC(C,i):
    return (C>>(2*i))&3

def decrC(C,i):
    v = getC(C,i)
    #assert(v>0)
    if not v&1:
        C = C^(1<<(2*i+1))
    return C^(1<<(2*i))

def encodeC(C):
    res = 0
    for i in xrange(len(C)-1,-1,-1):
        res = 4*res + C[i]
    return res

def initLC(G,LC):
    for c in xrange(len(G)):
        for i in xrange(K):
            LC[i][G[c][i]].append(c)


## Init
G = map((lambda s: map(int,list(s))), G)
N = len(G)
LC = [[[] for _ in xrange(V)] for _ in xrange(K)]
initLC(G,LC)
C0 = encodeC(C0)

def diffC(C1,C2):
    C = 0
    for k in xrange(N):
        #assert(getC(C1,k)>=getC(C2,k))
        C |= (getC(C1,k)-getC(C2,k))<<(2*k)
    return C


## Backtracking
memo = {}
def backtrack_first_half(C1,i=0,S=[]):
    if i==K/2:
        # on en memorise qu'un pour economiser la memoire
        # car on sait qu'il n'y aura qu'une unique solution
        if C1 not in memo:
            memo[C1] = tuple(S)
        return
    for a in xrange(V):
        avail = True
        for c in LC[i][a]:
            if getC(C1,c)==0:
                avail = False
                break
        if avail:
            C = C1
            for c in LC[i][a]:
                C = decrC(C,c)
            S.append(a)
            backtrack_first_half(C,i+1,S)
            S.pop()

def backtrack_second_half(C1,i=K/2,S=[]):
    if i==K:
        # on cherche une premiere moitie complementaire
        C = diffC(C0,C1)
        if C in memo:
            return list(memo[C])+S
        return None
    for a in xrange(V):
        avail = True
        for c in LC[i][a]:
            if getC(C1,c)==0:
                avail = False
                break
        if avail:
            C = C1
            for c in LC[i][a]:
                C = decrC(C,c)
            S.append(a)
            X = backtrack_second_half(C,i+1,S)
            if X!=None:
                return X
            S.pop()
    return None

## MAIN
def main():
    backtrack_first_half(C0)
    print ''.join(map(str,backtrack_second_half(C0)))

main()
