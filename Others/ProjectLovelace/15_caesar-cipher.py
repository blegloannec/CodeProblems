def break_caesar_cipher(ciphertext, known_word):
    known_word = known_word.lower()
    ciphertext = ciphertext.lower().split(' ')
    for k in range(26):
        plaintext = []
        for w in ciphertext:
            plaintext.append(''.join(chr((ord(c)-ord('a')+k)%26+ord('a')) if 'a'<=c<='z' else c for c in w))
        if known_word in plaintext:
            return ' '.join(plaintext)