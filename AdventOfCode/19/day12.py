#!/usr/bin/env pypy

E1 = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]     # Ex. 1
E2 = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]    # Ex. 2
I = [[-9, -1, -1], [2, 9, 5], [10, 18, -12], [-6, 15, -7]]  # Input


# Part 1
sgn = lambda x: 0 if x==0 else 1 if x>0 else -1

def simu(I, T):
    N,D = len(I),len(I[0])
    X = [L[:] for L in I]
    V = [[0]*D for _ in range(N)]
    for t in range(T):
        for i in range(N):
            for j in range(i+1,N):
                for k in range(D):
                    dv = sgn(X[i][k]-X[j][k])
                    V[i][k] -= dv
                    V[j][k] += dv
        for i in range(N):
            for k in range(D):
                X[i][k] += V[i][k]
    return sum(sum(map(abs,X[i]))*sum(map(abs,V[i])) for i in range(N))

#print(simu(E1,10))
#print(simu(E2,100))
print(simu(I,1000))


# Part 2
from fractions import gcd
lcm = lambda a,b: a*b//gcd(a,b)

def period(I):
    N,D = len(I),len(I[0])
    per = 1
    for k in range(D):
        X = [I[i][k] for i in range(N)]
        V = [0]*N
        t = 0
        Time = {}
        state = tuple(X+V)
        while state not in Time:
            Time[state] = t
            for i in range(N):
                for j in range(i+1,N):
                    dv = sgn(X[i]-X[j])
                    V[i] -= dv
                    V[j] += dv
            for i in range(N):
                X[i] += V[i]
            state = tuple(X+V)
            t += 1
        assert Time[state]==0  # no pre-period, strict cycle
        per = lcm(per, t)
    return per

#print(period(E1))
#print(period(E2))
print(period(I))
