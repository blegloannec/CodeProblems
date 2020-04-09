#!/usr/bin/env python3

N,M = map(int,input().split())
extra_edges = M-(N-1)
mst_cost = 0
curr_edge_cost = 1
for u in range(1,N):
    # we have u possible edges to link u with some v<u
    # we use one of them to connect u with the rest
    # (this one will be chosen in the MST)
    mst_cost += curr_edge_cost
    # and as many as the others to increase the current
    # edge cost (these will be discarded from the MST)
    curr_extra_edges = min(u-1, extra_edges)
    extra_edges -= curr_extra_edges
    curr_edge_cost += 1 + curr_extra_edges
print(mst_cost)
