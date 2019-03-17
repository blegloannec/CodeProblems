#!/usr/bin/env python3

# Greedy approach in O(sqrt(n))
# Key observations:
#  - It is always "optimal" to "upgrade" (buy new machines/workers)
#    as soon as possible: If the optimal requires to buy k ressources, then
#    there is clearly a way to achieve this optimal by buying progressively
#    the k ressources as fast as possible in a first phase, then accumulate
#    the candies till n is reached in a second phase.
#  - When buying a ressource, it is always optimal to reinforce the smallest
#    value between m and w: Indeed assuming m > w, we have m*(w+1) > (m+1)*w,
#    thus we should buy a worker.
# Approach: We simulate the first phase buying as much ressources as we can
# step by step (a "step" here is a minimal time lapse during enough candies
# are accumulated to buy a new ressource, each step is simulated in O(1))
# until we produce more than n in one time unit (m*w > n). At each step,
# we evaluate in O(1) the time taken for the phase 2 assuming we stop at that
# step to upgrade our production capacity. The optimal is the minimal overall
# time computed.
# This takes O(sqrt(n)) as this is the maximal number of steps needed to
# reach m ~ w ~ sqrt(n).

div_ceil = lambda n,q: (n + q-1)//q

if __name__=='__main__':
    # c the current number of candies, t the time
    c = t = 0
    m,w,p,n = map(int,input().split())
    if m<w:
        m,w = w,m
    res = div_ceil(n,m*w)
    while m*w < n:
        assert m>=w
        assert c<p
        # time needed to accumulate at least p candies to buy ressources
        dt = div_ceil(p-c,m*w)
        t += dt
        c += dt * m*w
        # buying a ressources
        a = c//p
        c %= p
        # attributing ressources to w < m
        d = m-w
        w0 = min(d,a)
        w += w0
        a -= w0
        # attributing remaining ressources equally to m ~ w
        a2w = a//2
        a2m = a-a2w
        m += a2m
        w += a2w
        # time to produce n candies with the current production capacity
        res = min(res, t+div_ceil(max(0,n-c),m*w))
    print(res)
