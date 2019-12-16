#!/usr/bin/env pypy

import sys

I = sys.stdin.readline().strip()
X0 = list(map(int,I))


# O(N log N)
def fft(X):
    N = len(X)
    S = [0] + X
    for i in xrange(1,N+1):
        S[i] += S[i-1]
    for i in xrange(N):
        k = i+1  # block size
        j = i    # starting index of the first 1-block
        c = 1    # 1/-1
        y = 0
        while j<N:
            y += c * (S[min(j+k,N)]-S[j])
            j += k<<1  # next 1/-1 block starting index
            c = -c
        X[i] = abs(y)%10
    return X


# Part 1
X = X0[:]
for _ in xrange(100):
    fft(X)
print(''.join(map(str,X[:8])))


# Part 2
offset = int(''.join(map(str,I[:7])))

def part2_general_case():
    X = X0*10000
    for i in xrange(100):
        sys.stderr.write('%d.. ' % (i+1))
        sys.stderr.flush()
        fft(X)
    sys.stderr.write('\n')
    return ''.join(map(str,X[offset:offset+8]))

# General case in ~ 100 N log N for N = 10^4, i.e. ~ 10^7
# runs in ~80s with pypy
#print(part2_general_case())


# Trick for the particular case of a large offset (near the end)
# (which seems to be the case for everyone according to the subreddit)
# The transform corresponds to the following linear map (-1/0/+1 matrix):
#  1 [+0-0+0-0+0-0+0-]
#  2 [0++00--00++00--]
#  3 [00+++000---000+]
#  4 [000++++0000----]
#  5 [0000+++++00000-]
#  6 [00000++++++0000]
#  7 [000000+++++++00]
#  8 [0000000++++++++]  -- second half --
#  9 [00000000+++++++]
# 10 [000000000++++++]
# 11 [0000000000+++++]
# 12 [00000000000++++]
# 13 [000000000000+++]
# 14 [0000000000000++]
# 15 [00000000000000+]

# 1. Obviously the index i of the fft(X) only depends on indices j>=i, hence
#    it is possible to compute the fft() of a suffix of size S in O(S log S).
def fft_suffix(X, i0=0):
    N = len(X)
    S = [0]
    for i in xrange(N-1,i0-1,-1):
        S.append(X[i]+S[-1])  # [0, sum(X[N-1:]), sum(X[N-2:]), ..., sum(X[i:])]
        k = i+1  # block size
        j = i    # starting index of the first 1-block
        c = 1    # 1/-1
        y = 0
        while j<N:
            l = len(S)-1-(j-i)
            y += c * (S[l]-S[max(0,l-k)])
            j += k<<1  # next 1/-1 block starting index
            c = -c
        X[i] = abs(y)%10
    return X

def part2_suffix():
    X = X0*10000
    for i in xrange(100):
        fft_suffix(X,offset)
    return ''.join(map(str,X[offset:offset+8]))

# runs in <1s with pypy
#print(part2_suffix())


# 2. Because offset is in the second half of the signal, this can still be
#    simplified as the values of fft() there simply are the suffix sums.
def part2_second_half_trick():
    X = X0*10000
    assert 2*offset>=len(X)
    X = X[offset:]
    for _ in range(100):
        for i in range(len(X)-2,-1,-1):
            X[i] = (X[i] + X[i+1]) % 10  # all X[i] are >= 0
    return ''.join(map(str,X[:8]))

print(part2_second_half_trick())
