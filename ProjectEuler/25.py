#!/usr/bin/env python

from math import *

def problem25():
    phi = (1+sqrt(5))/2
    print int(ceil((999+log10(sqrt(5)))/log10(phi)))

problem25()
