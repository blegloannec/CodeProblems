#!/usr/bin/env python3

W = {'C': 103.00919, 'F': 147.06841, 'L': 113.08406, 'V': 99.06841, 'I': 113.08406, 'H': 137.05891, 'P': 97.05276, 'R': 156.10111, 'E': 129.04259, 'W': 186.07931, 'Q': 128.05858, 'A': 71.03711, 'T': 101.04768, 'S': 87.03203, 'Y': 163.06333, 'K': 128.09496, 'D': 115.02694, 'M': 131.04049, 'G': 57.02146, 'N': 114.04293}

print(sum(W[c] for c in input()))
