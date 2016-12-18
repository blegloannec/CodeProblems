#!/usr/bin/env python

Input = '^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^'

# ECA rule 165, also NOT (left XOR right)
Rule = 165

def next_row(R):
    cpt,N = 0,[1]
    for i in xrange(1,len(R)-1):
        N.append((Rule>>((R[i-1]<<2) | (R[i]<<1) | R[i+1])) & 1)
        cpt += N[-1]
    N.append(1)
    return cpt,N

def count_safe(I,n):
    cpt,R = 0,[1]
    for c in I:
        R.append(int(c=='.'))
        cpt += R[-1]
    R.append(1)
    for _ in xrange(n-1):
        c,R = next_row(R)
        cpt += c
    return cpt

# Part One
print count_safe(Input,40)

# Part Two, uninteresting, would have been better with a
# twice smaller input but a way larger time to exploit the
# ultimate periodicity
print count_safe(Input,400000)
