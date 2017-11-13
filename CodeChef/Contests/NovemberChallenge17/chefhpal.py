#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        N,A = map(int,input().split())
        if A==1 or N==1:
            print(N,'a'*N)
        elif A==2:  # seul cas non trivial (mais facilement elucide
                    # en cherchant un peu a la main)
            if N==2:
                print(1,'ab')
            elif N<=4:
                print(2,'aabb'[:N])
            elif N<=8:
                print(3,'aaababbb'[:N])
            else:
                print(4,'aababb'*(N//6)+'aababb'[:N%6])
        else:
            print(1,'abc'*(N//3)+'abc'[:N%3])

main()
