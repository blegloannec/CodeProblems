#!/usr/bin/env python

N = [1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
M = [sum(N[i:]) for i in range(len(N))]
M.append(0)
#N = range(1,6)+range(7,12)
T = sum(N)
S = T/3
S2 = T/4

# progdyn pour 3-partition
memo = {}
def progdyn(n,s1,s2):
    if s1<0 or s2<0 or T-s1-s2-M[n+1]<0:
        return (10000000,0)
    if n<0:
        if s1==0 and s2==0:
            return (0,1)
        return (10000000,0)
    h = (n,s1,s2)
    if h in memo:
        return memo[h]
    x1,y1 = progdyn(n-1,s1-N[n],s2)
    res = min([(x1+1,y1*N[n]),progdyn(n-1,s1,s2-N[n]),progdyn(n-1,s1,s2)])
    memo[h] = res
    return res

# Version 2 pour 4-partition
# Amusant : marche moins bien que le version a 5 params du 19.py
# la raison est que l'espace est ici reduit d'a la louche 1/4 de base
# mais l'optim du tri sur (s2,s3) ne le divise que par 2
# (d'ou du 3/8 au final)
# alors que dans la version a 5 params, il divise par 3!=6
# par le tri (d'ou du 1/6 au final)
memo2 = {}
def progdyn2(n,s1,s2,s3):
    m = min(s2,s3)
    h = (n,s1,s2,s2+s3-m)
    if h in memo2:
        return memo2[h]
    if s1<0 or s2<0 or s3<0 or T-s1-s2-s3-M[n+1]<0:
        return (10000000,0)
    if n<0:
        if (s1,s2,s3)==(0,0,0):
            return (0,1)
        return (10000000,0)
    x1,y1 = progdyn2(n-1,s1-N[n],s2,s3)
    res = min([(x1+1,y1*N[n]),progdyn2(n-1,s1,s2-N[n],s3),progdyn2(n-1,s1,s2,s3-N[n]),progdyn2(n-1,s1,s2,s3)])
    memo2[h] = res
    return res

def main():
    #print progdyn(len(N)-1,S,S)
    #print len(memo)
    print progdyn2(len(N)-1,S2,S2,S2)
    print len(memo2)
    
main()
