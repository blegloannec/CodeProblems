#!/usr/bin/env python

# Classical Nim

cpt = 0
for i in xrange(1,(1<<30)+1):
    if i^(2*i)^(3*i)==0:
        cpt += 1
print cpt

# NB a posteriori : remarque de koen sur le forum
# "Turns out, it's all numbers that don't have two consecutive ones
# in it's binary representation.
# That makes the answer fibonacci(32)"
