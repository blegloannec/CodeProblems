#!/usr/bin/env python3

import sys
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad

if __name__=='__main__':
    if len(sys.argv)!=3:
        sys.stderr.write(f'usage: {sys.argv[0]} solution path/to/encrypted_code > source_code\n')
        sys.exit(1)
    solution = sys.argv[1].strip()
    H = SHA256.new(solution.encode()).digest()
    Key,IV = H[:16],H[16:]
    C = open(sys.argv[2], 'rb').read()
    M = unpad(AES.new(Key, AES.MODE_CBC, iv=IV).decrypt(b64decode(C)), 16)
    sys.stdout.write(M.decode())
