# Project Euler

![PE Profile](https://projecteuler.net/profile/NiakTheWizard.png)

**Disclaimer:** To protect this repository from cheaters, the codes are encrypted and you need the right answer to each problem to decrypt the associated code.
 - First, the solution, seen as a string, is SHA-256 hashed.
 - The first 16 bytes of the hash are used as the Key and the last 16 bytes as the Initialization Vector for an AES-128 CBC encryption of the PKCS#7-padded source code.
 - Finally, the encrypted data is base64 encoded.
 
The script `pe_encrypt.py` was used to execute that process, `pe_decrypt.py` can be used to decrypt.

**Language:** Generally Python 2/3 with the fast interpreter `pypy`. Sometimes C++. Only occasionally (for various reasons) OCaml, Prolog, Julia, Lua and some help from Sage...

Almost all of these codes are below the *one-minute rule* (usually by far), though they are not necessarily optimal or optimized (they are sometimes just good enough considering the input size).

More efficient implementations of some of these codes are in `/HackerRank/Contests/ProjectEuler+` (harder variants of the problems, with larger inputs, generally requiring an optimal approach).

**Fun additional constraints:**
 * Problem 307, *Chip Defects*, was solved on an "actual" low-cost [ESP8266](https://en.wikipedia.org/wiki/ESP8266) chip (80MHz CPU), using the NodeMCU (Lua-based) firmware. It ran in 0.7s and fortunately my chip did not seem to have any defects!

**Interesting links:**
 * [OEIS](http://oeis.org/)
 * [Quadratic (two variable) Diophantine equation solver](https://www.alpertron.com.ar/QUAD.HTM) (particularly useful when not reducible to the [Pell-Fermat case](https://en.wikipedia.org/wiki/Pell%27s_equation))
 * [Custom Grid Paper generator](http://incompetech.com/graphpaper/)
 