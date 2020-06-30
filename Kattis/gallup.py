#!/usr/bin/env python3

def main():
    t = 1
    while True:
        P = input()
        if P=='0':
            break
        P = P.split()[1:]
        D = len(P[0])-1-P[0].index('.') if '.' in P[0] else 0
        p10 = 10**(D+3)
        P = [10*int(p.replace('.','')) for p in P]
        res = 'error'
        for N in range(1,10000):
            L = R = 0
            for p in P:
                # p-5 <= p10*n/N < p+5
                # N(p-5)/p10 <= n < N(p+5)/p10
                L += (N*(p-5) + p10-1)//p10
                R += (N*(p+5) - 1)//p10
            if L<=N<=R:
                res = N
                break
        print(f'Case {t}: {res}')
        t += 1

main()
