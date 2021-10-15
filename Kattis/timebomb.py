#!/usr/bin/env python3

D = [31599, 4681, 29671, 29647, 23497, 31183, 31215, 29257, 31727, 31695]

def digits(S):
    return [int(''.join(L[4*k:4*k+3] for L in S).replace(' ','0').replace('*','1'), 2) \
            for k in range((len(S[0])+1)//4)]

def main():
    S = [input() for _ in range(5)]
    t = 0
    for d in digits(S):
        try:
            t = 10*t + D.index(d)
        except ValueError:
            t = 1
            break
    print('BEER!!' if t%6==0 else 'BOOM!!')

main()
