As it is a solution to a pretty difficult ongoing competitive challenge, the file `nintendo_c.cpp` is XOR-encrypted.

If you want to read it, consider the solution of the problem to the following input fo size 512 (yeah!):
```
512
33188243 e7af2633 fb8fec83 a3ef0abc e3a18b2f ad40cfdd f0a3503e 5c933029 0ec2e76c eda21bc3 ec09898e 4ab13684 a89965ac af890d4c 15371b8f f6c6e7c8 3194e498 38a447bb 65794c14 382389aa 6cb66a74 8f4f227d b6ae8ca7 f06d8231 6a4dd948 76ae2819 40015afb 5c8700d2 cf5854ea 4679e3a7 a4bafdcd 6ba5c9fb
```
(this is the concatenation of the SHA-512 hashes or the strings `nintendo` and `NIN10DO`)


Now remove all the whitespace characters from it to get a single hexadecimal string. That string has been used to encrypt the code using the following basic XOR encryption/decryption algorithm:
```
#!/usr/bin/env python3

import sys

key = open(sys.argv[1],'r').read().strip()
K = [int(key[i*2:(i+1)*2],16) for i in range(len(key)//2)]
i = 0
for c in sys.stdin.read():
    sys.stdout.write(chr(ord(c)^K[i]))
    i = (i+1)%len(K)
```

The MD5 hash of the decrypted file is `ad74df0e65f886f65edb4550296684c3`.
