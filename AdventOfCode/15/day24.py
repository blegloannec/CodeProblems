#!/usr/bin/env python

N = [1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
#N = range(1,6)+range(7,12)
S = sum(N)/3
S2 = sum(N)/4

# progdyn pour 3-partition
memo = {(-1,0,0,0):(0,1)}
def progdyn(n,s1,s2,s3):
    if s1<0 or s2<0 or s3<0:
        return (10000000,0)
    h = (n,s1,s2,s3)
    if h in memo:
        return memo[h]
    x1,y1 = progdyn(n-1,s1-N[n],s2,s3)
    res = min([(x1+1,y1*N[n]),progdyn(n-1,s1,s2-N[n],s3),progdyn(n-1,s1,s2,s3-N[n])])
    memo[h] = res
    return res

# Version pour 4-partition
# par symetrie on trie les paquets 2,3,4
# pour economiser l'espace
memo2 = {(-1,0,(0,0,0)):(0,1)}
def progdyn2(n,s1,s2,s3,s4):
    if s1<0 or s2<0 or s3<0 or s4<0:
        return (10000000,0)
    h = (n,s1,tuple(sorted([s2,s3,s4])))
    if h in memo2:
        return memo2[h]
    x1,y1 = progdyn2(n-1,s1-N[n],s2,s3,s4)
    res = min([(x1+1,y1*N[n]),progdyn2(n-1,s1,s2-N[n],s3,s4),progdyn2(n-1,s1,s2,s3-N[n],s4),progdyn2(n-1,s1,s2,s3,s4-N[n])])
    memo2[h] = res
    return res

def main():
    #print progdyn(len(N)-1,S,S,S)
    #print len(memo)
    print progdyn2(len(N)-1,S2,S2,S2,S2)
    print len(memo2)
    
main()
