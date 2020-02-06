#!/usr/bin/env python3

# (a,b) with a<=b --> ordered (2a,b-a)
# 1. 2a + b-a = a+b the sum is always preserved, hence there is a finite
#    number of reachable couples and the sequence has to loop or halt.
# 2. For any c and for any d dividing both a_0 and b_0,
#    the sequence starting by (c*a_0, c*b_0) is (c*a_n, c*b_n)_n
#                             (a_0/d, b_0/d)    (a_n/d, b_n/d)_n
#    Hence it is equivalent to always simplify the terms by their gcd,
#    i.e. study the iterations through the following **modified map**:
#    (a,b) with a<=b, gcd(a,b)=1 --> ordered (2a/g,(b-a)/g) with g = gcd(2a,b-a)
# 3. If gcd(a,b) = 1, then gcd(2a,b-a) = 1 or 2 (depending on the parity of b-a)
#    hence the modified map either preserves the sum or divides it by 2.
#    The iterations stop iff we reach (1,1) of sum 2, hence the initial sum
#    had to be a power of 2.
# 4. The converse is easy to prove: Say at any given step we have a+b = 2^k even
#    and gcd(a,b) = 1. If k = 1, then a = b = 1 and it stops.
#    Otherwise k>1, a and b are both odd, 2a and b-a are even, gcd(2a,b-a) = 2,
#    we simplify by 2 and get a & (b-a)/2 both odd of sum 2^(k-1)
#    and the story repeats...
# => It halts iff the initial sum for the modified map, i.e. after
#     simplification by the gcd, is a power of 2.

from math import gcd

is_pow2 = lambda x: x&(x-1)==0
halts = lambda a,b: is_pow2((a+b)//gcd(a,b))

N = int(input())
for _ in range(N):
    a,b = map(int,input().split())
    print('halts' if halts(a,b) else 'loops')
