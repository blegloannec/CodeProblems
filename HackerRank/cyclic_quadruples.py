#!/usr/bin/env python3

MOD = 10**9+7

def main():
    T = int(input())
    for _ in range(T):
        L1,R1,L2,R2,L3,R3,L4,R4 = map(int,input().split())
        R1,R2,R3,R4 = R1+1,R2+1,R3+1,R4+1
        # all quadruples
        Res  = (R1-L1)*(R2-L2)*(R3-L3)*(R4-L4)
        # inclusion-exclusion
        Res -= max(0, min(R1,R2)-max(L1,L2)) * (R3-L3)*(R4-L4)
        Res -= max(0, min(R2,R3)-max(L2,L3)) * (R1-L1)*(R4-L4)
        Res -= max(0, min(R3,R4)-max(L3,L4)) * (R1-L1)*(R2-L2)
        Res -= max(0, min(R4,R1)-max(L4,L1)) * (R2-L2)*(R3-L3)
        # 2-by-2 intersections
        Res += max(0, min(R1,R2,R3)-max(L1,L2,L3)) * (R4-L4)
        Res += max(0, min(R1,R2,R4)-max(L1,L2,L4)) * (R3-L3)
        Res += max(0, min(R1,R3,R4)-max(L1,L3,L4)) * (R2-L2)
        Res += max(0, min(R2,R3,R4)-max(L2,L3,L4)) * (R1-L1)
        Res += max(0, min(R1,R2)-max(L1,L2)) * max(0, min(R3,R4)-max(L3,L4))
        Res += max(0, min(R2,R3)-max(L2,L3)) * max(0, min(R4,R1)-max(L4,L1))
        # 3-by-3 intersections (4 identical ones)
        #Res -= 4*max(0, min(R1,R2,R3,R4)-max(L1,L2,L3,L4))
        # full intersection (same as 3-by-3)
        #Res += max(0, min(R1,R2,R3,R4)-max(L1,L2,L3,L4))
        # simplification
        Res -= 3*max(0, min(R1,R2,R3,R4)-max(L1,L2,L3,L4))
        print(Res % MOD)

main()
