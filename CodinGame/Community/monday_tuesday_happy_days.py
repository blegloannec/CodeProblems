#!/usr/bin/env python3

LM = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
MS = [31,28,31,30,31,30,31,31,30,31,30,31]
LD = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

leap = input()=='1'
if leap:
    MS[1] = 29
D1,M1,N1 = input().split()
D1,M1,N1 = LD.index(D1),LM.index(M1),int(N1)-1
M2,N2 = input().split()
M2,N2 = LM.index(M2),int(N2)-1

nd1 = sum(MS[:M1]) + N1
nd2 = sum(MS[:M2]) + N2
print(LD[(nd2-nd1+D1)%7])
