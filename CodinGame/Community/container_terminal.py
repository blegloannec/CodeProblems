#!/usr/bin/env python3

# Smallest partition into decreasing chains.
# Can be done greedily in O(n × #chains) by always pushing the current
# element Ai above the smallest top Ak, k < i, of a current stack such
# that Ai ≤ Ak (if any).
# This is indeed optimal as in any other solution from there, let Al be
# the element below Ai (if any), we have Ai ≤ Ak ≤ Al by definition of Ak,
# hence the stacks held by Ak and Al can simply be swapped without
# changing the total number of stacks, building an equivalent solution
# where Ai is above Ak.

# Note that this process maintains the tops of the current stacks
# in increasing order. Hence it can be improved to O(n × log #chains)
# using binary search to find the appropriate stack at each step.

# This approach is similar to the Longest Increasing Subsequence problem:
#  https://en.wikipedia.org/wiki/Longest_increasing_subsequence
# Indeed both problems are dual through Dilworth's theorem:
#  https://en.wikipedia.org/wiki/Dilworth's_theorem
# Decreasing stacks are the chains for the custom order:
#   Aj ≺ Ai  <=>  i < j  &  Aj ≤ Ai
# while incr. subseq. exactly are the antichains.
# By Dilworth, the size of the smallest partition into stacks is
# exactly the size of a LIS.

N = int(input())
for _ in range(N):
    Stacks = []
    for c in input():
        stacked = False
        for stack in Stacks:
            if stack[-1]>=c:
                stack.append(c)
                stacked = True
                break
        if not stacked:
            Stacks.append([c])
    print(len(Stacks))
