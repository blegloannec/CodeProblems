#!/usr/bin/env python3

# basic timing leak attack, see also cryptopals 4.31-32

import sys
import string, random
random.seed()
Alpha = list(string.ascii_letters + string.digits)
random.shuffle(Alpha)

def send_recv(pwd):
    sys.stdout.write(pwd + '\n')
    sys.stdout.flush()
    ans = sys.stdin.readline().split()
    if ans[1][0]=='G':      # ACCESS GRANTED
        sys.exit(0)
    return int(ans[2][1:])  # ACCESS DENIED (** ms)

def main():
    # Guess size
    L = 1
    while send_recv(L*Alpha[0]) <= 5:
        L += 1
    # Guess password
    P = [Alpha[0]]*L
    for i in range(L):
        for a in Alpha:
            P[i] = a
            if send_recv(''.join(P)) > 5+(i+1)*9:
                break

main()
