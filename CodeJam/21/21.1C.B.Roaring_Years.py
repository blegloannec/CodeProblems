#!/usr/bin/env python3

roar = lambda n: lambda x0: int(''.join(map(str, range(x0, x0+n))))

# NB: roar(14)(1) is the next roaring number after 10^18

def main():
    T = int(input())
    for t in range(1, T+1):
        Y = int(input())
        res = float('inf')
        for n in range(2, 15):
            R = roar(n)
            l = 1; r = 10**(19//n)
            while l<r:
                m = (l+r)//2
                if R(m)<=Y:
                    l = m+1
                else:
                    r = m
            res = min(res, R(l))
        print(f'Case #{t}: {res}')

main()
