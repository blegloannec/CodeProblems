The file `nintendo_c.cpp` is XOR-encrypted as it is a solution to a pretty difficult ongoing competitive challenge.

To access it, consider the problem expected output to the following input of size 512 (yeah!):
```
512
33188243 e7af2633 fb8fec83 a3ef0abc e3a18b2f ad40cfdd f0a3503e 5c933029 0ec2e76c eda21bc3 ec09898e 4ab13684 a89965ac af890d4c 15371b8f f6c6e7c8 3194e498 38a447bb 65794c14 382389aa 6cb66a74 8f4f227d b6ae8ca7 f06d8231 6a4dd948 76ae2819 40015afb 5c8700d2 cf5854ea 4679e3a7 a4bafdcd 6ba5c9fb
```
(which is the concatenation of the SHA-512 hashes of the strings `nintendo` and `NIN10DO`)

Now remove all the whitespace characters from that output to get a single hexadecimal string. That string has been used as the key to encrypt the code using the following basic XOR encryption/decryption `python3` lines (see `xorcat.py`):
```
K = bytes.fromhex(open(sys.argv[1],'r').read().strip())
M = sys.stdin.buffer.read()
sys.stdout.buffer.write(bytes(c^k for c,k in zip(M,itertools.cycle(K))))
```

The MD5 hash of the decrypted file is `d1fc8764673110e1384929ef45343252`.
