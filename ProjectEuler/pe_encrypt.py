#!/usr/bin/env python3

import sys
from base64 import b64encode
from hashlib import sha256
from Crypto.Cipher import AES

def AES_CBC_encrypt(Key, IV, M):
    C = AES.new(Key,AES.MODE_CBC,IV)
    return C.encrypt(M)

def PKCS7_pad(M, BS=16):
    r = len(M)%BS
    M += bytes([BS-r]*(BS-r))
    return M

if __name__=='__main__':
    if len(sys.argv)!=3:
        sys.stderr.write('usage: %s solution /path/to/source_file > encrypted_code\n' % sys.argv[0])
        sys.exit(1)
    solution = sys.argv[1]
    H = sha256(solution.encode()).digest()
    Key,IV = H[:16],H[16:]
    F = open(sys.argv[2],'rb')
    M = F.read()
    C = b64encode(AES_CBC_encrypt(Key,IV,PKCS7_pad(M)))
    sys.stdout.write(C.decode())
    F.close()
