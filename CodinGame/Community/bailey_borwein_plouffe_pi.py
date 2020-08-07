#!/usr/bin/env python3

# π = ∑ₖ 1/16^k (4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))
#   = lim_k 4S₁(k) - 2S₄(k) - S₅(k) - S₆(k)
# when interested into the (i+1)th hex-digit of Sₐ,
# we need the fractional part (or at least its first digit) of:
# 16^i * Sₐ(k) = ∑ₖ 16^(i-k) / (8k+a)
#              = ∑_{k=0..i} 16^(i-k)/(8k+a) + ∑_{k=i+1..} 16^(i-k)/(8k+a)
# Only the first sum terms can be > 1, and of course be huge, but can
# be dealt with by computing 16^(i-k) mod (8k+a), as if 16^(i-k) = q(8k+a)+r,
# then 16^(i-k)/(8k+a) = q + r/(8k+a) and we can throw away the integer q.
# The second sum converges quickly.

def S(a, i):
    s = 0.
    for k in range(i):
        s += pow(16, i-k, 8*k+a) / (8.*k+a)
    for k in range(i, i+20):
        s += 16.**(i-k) / (8.*k+a)
    return s % 1

def P(i):
    return int(16*(4*S(1,i) - 2*S(4,i) - S(5,i) - S(6,i)) % 16)

i = int(input())
print(P(i-1))
