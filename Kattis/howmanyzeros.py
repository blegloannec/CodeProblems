#!/usr/bin/env python3

# total count of 0s of k-digit numbers, leading 0s allowed
def full_cnt0(k):
    return 0 if k<=0 else k * 10**(k-1)

# total count of 0s of k-digit numbers, no leading 0s
def all_cnt0(k):
    return int(k==1) if k<=1 else (k-1) * 9 * 10**(k-2)

# DP for the count of 0s in numbers <=n
def cnt0(n):
    if n<=0:
        return int(n==0)
    D = list(map(int,reversed(str(n))))
    S = 1  # count of 0s
    C = 1  # count of numbers in S
    for k,d in enumerate(D):
        if d==0:
            S += C
        else:
            S += (d-1) * full_cnt0(k)
            C += (d-1) * 10**k
            if k<len(D)-1:
                S += 10**k + full_cnt0(k)
                C += 10**k
    for k in range(2,len(D)):
        S += all_cnt0(k)
    return S

def main():
    while True:
        a,b = map(int,input().split())
        if a<0:
            break
        print(cnt0(b) - cnt0(a-1))

main()
