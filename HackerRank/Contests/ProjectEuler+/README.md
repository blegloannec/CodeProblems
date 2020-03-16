# Project Euler+

**Disclaimer:** The codes are encrypted and you need the answer to each corresponding Project Euler problem to decrypt the associated code.
 - First, the solution, seen as a string, is SHA-256 hashed.
 - The first 16 bytes of the hash are used as the Key and the last 16 bytes as the Initialization Vector for an AES-128 CBC encryption of the PKCS#7-padded source code.
 - Finally, the encrypted data is base64 encoded.
 
The script `/ProjectEuler/pe_encrypt.py` was used to execute that process, `/ProjectEuler/pe_decrypt.py` can be used to decrypt.
