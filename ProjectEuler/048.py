#!/usr/bin/env python

# In general, modular fast exp, but here :-)
print sum([(i**i)%10000000000 for i in xrange(1,1001)])%10000000000
