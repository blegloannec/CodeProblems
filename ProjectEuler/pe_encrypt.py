#!/usr/bin/env python3

import sys
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad

if __name__=='__main__':
    if len(sys.argv)!=3:
        sys.stderr.write(f'usage: {sys.argv[0]} solution /path/to/source_file > encrypted_code\n')
        sys.exit(1)
    solution = sys.argv[1].strip()
    H = SHA256.new(solution.encode()).digest()
    Key,IV = H[:16],H[16:]
    M = open(sys.argv[2], 'rb').read()
    C = b64encode(AES.new(Key, AES.MODE_CBC, iv=IV).encrypt(pad(M, 16)))
    sys.stdout.write(C.decode())
