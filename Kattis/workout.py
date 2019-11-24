#!/usr/bin/env python3

M = 10
C = 3

def main():
    UR = tuple(map(int,input().split()))
    JimUse, JimRec = UR[::2], UR[1::2]
    MacUse, MacRec, T = zip(*(map(int,input().split()) for _ in range(M)))
    T = list(T)
    m = t = 0
    for _ in range(C*M):
        if t>=T[m]:
            q = (t-T[m])//(MacUse[m]+MacRec[m]) + 1
            T[m] += q*(MacUse[m]+MacRec[m])
            t = max(t, T[m]-MacRec[m])
        T[m] = max(T[m], t+JimUse[m])
        t += JimUse[m] + JimRec[m]
        m = (m+1) % M
    t -= JimRec[M-1]
    print(t)

main()
