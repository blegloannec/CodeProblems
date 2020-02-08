#!/usr/bin/env python3

P = 10**9+7

def tilings1(N):
    return int(N%3==0)

C2 = [1,0,1,1]
def tilings2(N):
    while len(C2)<=N:
        C2.append((C2[-2]+C2[-3]) % P)
    return C2[N]

C3 = [1,1,1,2]
S3 = [1,1,1,3]
C3_011 = [0,0,0,1]
def tilings3(N):
    while len(C3)<=N:
        # ┌─┨   ┌─────┨   ┌─────┨
        # │ ┃ + ├─────┨ + └─┬───┨ & up/down symmetry
        # │ ┃   ├─────┨     │   ┃
        # └─┨   └─────┨     └───┨
        C3.append((C3[-1] + C3[-3] + 2*C3_011[-3]) % P)
        # ┌─────┨       ┌╌╌╌╌╌┬╌╌╌╌╌┬─────┨
        # └─┬───┺━┓ + ∑ ├───┬╌┴╌╌╌┬╌┴───┬─┺━┓
        #   ├─────┨     │   ├╌╌╌╌╌┼╌╌╌╌╌┤   ┃
        #   └─────┨     └───┴╌╌╌╌╌┴╌╌╌╌╌┴───┨
        C3_011.append((C3_011[-3] + S3[-3]) % P)
        # S3[n] = ∑ C3[n-3k]
        S3.append((C3[-1] + S3[-3]) % P)
    return C3[N]

tilings = (tilings1, tilings2, tilings3)

def main():
    T = int(input())
    for _ in range(T):
        K,N = map(int,input().split())
        print(tilings[K-1](N))

main()
