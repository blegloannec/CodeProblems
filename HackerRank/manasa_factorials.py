#!/usr/bin/env python3

# the number of 0 at the end of m! is the power of 5 in its
# primal decomposition: 10^min(val2(m!),val5(m!)) = 10^val5(m!)
# which gives val5(m!) 0s
def fact0(m):
    cpt = 0
    p5 = 5
    while p5<=m:
        cpt += m//p5
        p5 *= 5
    return cpt

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        # dichotomic search for the optimal
        a,b = 0,1<<56
        while a<b:
            m = (a+b)//2
            if fact0(m)<n:
                a = m+1
            else:
                b = m
        print(a)

main()
