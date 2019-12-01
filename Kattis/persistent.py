#!/usr/bin/env python3

def main():
    while True:
        N = int(input())
        if N==0:
            print(10)
            continue
        elif N<0:
            break
        D = []
        for d in range(9,1,-1):
            while N%d==0:
                D.append(d)
                N //= d
        while len(D)<2:
            D.append(1)
        if N>1:
            print('There is no such number.')
        else:
            print(''.join(map(str,reversed(D))))

main()
