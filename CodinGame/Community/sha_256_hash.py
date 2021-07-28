#!/usr/bin/env python3

rot = lambda n,r: (n>>r) | ((n&((1<<r)-1))<<(32-r))  # int32 right rotate

# https://en.wikipedia.org/wiki/SHA-2#Pseudocode

# Note 1: All variables are 32 bit unsigned integers and addition is calculated modulo 2^32
# Note 2: For each round, there is one round constant k[i] and one entry
#         in the message schedule array w[i], 0 ≤ i ≤ 63
# Note 3: The compression function uses 8 working variables, a through h
# Note 4: Big-endian convention is used when expressing the constants in this pseudocode,
#         and when parsing message block data from bytes to words, for example,
#         the first word of the input message "abc" after padding is 0x61626380

def sha256(M : bytes) -> bytes:
    # Initialize hash values
    # (first 32 bits of the fractional parts of the square roots of the first 8 primes 2..19)
    #H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19] # standard
    H = [0xcbbb9d5d, 0x629a292a, 0x9159015a, 0x152fecd8, 0x67332667, 0x8eb44a87, 0xdb0c2e0d, 0x47b5481d]  # custom

    # Initialize array of round constants
    # (first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311):
    K = (0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
         0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
         0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
         0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
         0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
         0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
         0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
         0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2)

    msk32 = (1<<32)-1

    # Pre-processing (Padding)
    # begin with the original message of length L bits
    # append a single '1' bit
    # append K '0' bits, where K is the minimum number >= 0 such that L + 1 + K + 64 is a multiple of 512
    # append L as a 64-bit big-endian integer, making the total post-processed length a multiple of 512 bits
    # such that the bits in the message are L 1 00..<K 0's>..00 <L as 64 bit integer> = k*512 total bits
    M = bytearray(M)
    l = len(M)
    k = (-(l+1+8)) % 64
    M.append(1<<7)
    M += bytes(k)
    M += (8*l).to_bytes(8, 'big')

    # Process the message in successive 512-bit chunks
    B = [int.from_bytes(M[i:i+4], 'big') for i in range(0, len(M), 4)]
    for b in range(0, len(B), 16):
        # create a 64-entry message schedule array w[0..63] of 32-bit words
        # (The initial values in w[0..63] don't matter, so many implementations zero them here)
        # copy chunk into first 16 words w[0..15] of the message schedule array
        W = B[b:b+16] + [0]*48

        # Extend the first 16 words into the remaining 48 words w[16..63] of the message schedule array
        for i in range(16, 64):
            s0 = rot(W[i-15],  7) ^ rot(W[i-15], 18) ^ (W[i-15]>> 3)
            s1 = rot(W[i- 2], 17) ^ rot(W[i- 2], 19) ^ (W[i- 2]>>10)
            W[i] = (W[i-16] + s0 + W[i-7] + s1) & msk32

        # Initialize working variables to current hash value
        a,b,c,d,e,f,g,h = H

        # Compression function main loop
        for i in range(64):
            s1 = rot(e, 6) ^ rot(e, 11) ^ rot(e, 25)
            ch = (e & f) ^ (~e & g)
            tmp1 = (h + s1 + ch + K[i] + W[i]) & msk32
            s0 = rot(a, 2) ^ rot(a, 13) ^ rot(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            tmp2 = (s0 + maj) & msk32
 
            h = g
            g = f
            f = e
            e = (d + tmp1) & msk32
            d = c
            c = b
            b = a
            a = (tmp1 + tmp2) & msk32

        # Add the compressed chunk to the current hash value
        for i,x in enumerate((a,b,c,d,e,f,g,h)):
            H[i] = (H[i] + x) & msk32

    # Produce the final hash value (big-endian)
    return b''.join(h.to_bytes(4, 'big') for h in H)

print(sha256(input().encode()).hex())
