#!/usr/bin/env pypy

I = '380621'


# Part 1
def part1(I):
    I = int(I)
    a,b = 0,1
    R = [3,7]
    while len(R)<I+10:
        x = R[a]+R[b]
        if x>=10:
            R.append(1)
        R.append(x%10)
        a = (a+R[a]+1)%len(R)
        b = (b+R[b]+1)%len(R)
    return ''.join(map(str,R[I:I+10]))

print(part1(I))


# Part 2
def part2(I):
    I = list(map(int,I))
    a,b = 0,1
    R = [3,7]
    while True:
        x = R[a]+R[b]
        if x>=10:
            R.append(1)
            if len(R)>=len(I) and R[-len(I):]==I:
                break
        R.append(x%10)
        if len(R)>=len(I) and R[-len(I):]==I:
            break
        a = (a+R[a]+1)%len(R)
        b = (b+R[b]+1)%len(R)
    return len(R)-len(I)

print(part2(I))
