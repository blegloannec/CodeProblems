#!/usr/bin/env python3

import sys
from base64 import b64decode
from hashlib import sha256
from Crypto.Cipher import AES

def AES_CBC_decrypt(Key, IV, M):
    C = AES.new(Key,AES.MODE_CBC,IV)
    return C.decrypt(M)

def PKCS7_unpad(M, BS=16):
    assert len(M)%BS==0
    if M and M[-1]<BS:
        assert all(M[i]==M[-1] for i in range(len(M)-M[-1],len(M)-1))
        M = M[:-M[-1]]
    return M

if __name__=='__main__':
    if len(sys.argv)!=3:
        sys.stderr.write('usage: %s solution path/to/encrypted_code > source_code\n' % sys.argv[0])
        sys.exit(1)
    solution = sys.argv[1]
    H = sha256(solution.encode()).digest()
    Key,IV = H[:16],H[16:]
    F = open(sys.argv[2],'rb')
    C = F.read()
    M = PKCS7_unpad(AES_CBC_decrypt(Key,IV,b64decode(C)))
    sys.stdout.write(M.decode())
    F.close()
