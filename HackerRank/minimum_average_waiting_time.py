#!/usr/bin/env python3

# minimizing average lateness
# this is a "1 | r_j; (p_j qcq) | avg L_j" scheduling problem
# or equivalently "1 | r_j | sum L_j"
# for r_j the release times and L_j = C_i - r_j the lateness
# this is actually equivalent to the mean flow time pb and is
# minimized by a Shortest Processing Time greedy approach

# The crucial point is the following:
#   Let us consider an optimal planning and a time T in that planning where K
#   tasks A are available, i.e. there are K tasks that are not yet executed
#   and such that r_k <= T. Let us assume that:
#     - task j in A is executed at time T in that optimal planning;
#     - there exists a task i in A such that pi <= pj.
#   Let us prove that it is also optimal to execute i at time T.
#   Indeed, the total induced contribution of "planning j at T" to the
#   lateness sum is:
#     Cj = K*pj + sum(T + pj - rl for all tasks l such that T < rl < T+pj)
#   while planning i at T would contribute:
#     Ci = K*pi + sum(T + pi - rl for all tasks l such that T < rl < T+pi)
#   but, as pi <= pj, we have Ci <= Cj (as the sum Cj contains at last the
#   same terms as Ci) hence it would be optimal as well to plan i at time T.
#   Thus, it is optimal to always plan the shortest available task.

from heapq import *

N = int(input())
C = sorted(tuple(map(int,input().split())) for _ in range(N))

t = i = sumL = 0
H = []
while H or i<len(C):
    while i<len(C) and C[i][0]<=t:
        r,p = C[i]
        heappush(H,(p,r))
        i += 1
    if H:
        p,r = heappop(H)
        t += p
        sumL += t-r
    else:
        t = C[i][0]
print(sumL//N)
