#!/usr/bin/env python3

P = list(map(int,input().split(',')))

def run(P, noun=12, verb=2):
    P = P[:]  # copy
    P[1], P[2] = noun, verb
    for i in range(0,len(P),4):
        op,p1,p2,p3 = P[i:i+4]
        if op==1:
            P[p3] = P[p1]+P[p2]
        elif op==2:
            P[p3] = P[p1]*P[p2]
        else:
            assert op==99
            break
    return P[0]

print(run(P))


# Part 2
def part2():
    for noun in range(100):
        for verb in range(100):
            if run(P,noun,verb)==19690720:
                return 100*noun+verb

print(part2())
