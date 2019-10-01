#!/usr/bin/env python3

# total sum of digits of k-digit numbers (0 to 10^k-1)
def fullsum(k):
    # 0+1+...+9 = 45
    return 0 if k<=0 else 45*k*10**(k-1)

# DP for the sum of all digits in numbers <=n
# following implementation in O(log^2 n)
# but could easily be optimized down to O(log n)
def digsum(n):
    if n<=0:
        return 0
    D = list(map(int,reversed(str(n))))
    S = 0  # sum
    C = 1  # count
    for k,d in enumerate(D):
        S += d*C             # + (k+1)-digit numbers starting with d
        #for x in range(d):  # + (k+1)-digit numbers starting with x<d
        #    S += x*10**k + fullsum(k)
        S += (d-1)*d//2 * 10**k + d * fullsum(k)
        C += d*10**k
    return S

def main():
    T = int(input())
    for _ in range(T):
        a,b = map(int,input().split())
        print(digsum(b) - digsum(a-1))

main()
