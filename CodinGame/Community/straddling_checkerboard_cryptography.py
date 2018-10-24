#!/usr/bin/env python3

from itertools import cycle

# historically interesting problem
# https://en.wikipedia.org/wiki/VIC_cipher
class VIC:
    def __init__(self, header, passphrase, pos_slash, pos_dot):
        assert(len(passphrase)==10)
        assert(all(c==' ' or 'A'<=c<='Z' for c in passphrase))
        self.Header = list(map(int,header))
        self.Space = [self.Header[i] for i in range(10) if passphrase[i]==' ']
        assert(len(self.Space)==2 and self.Space[0]>0)
        self.Board = {'/': self.Header[pos_slash]+10*self.Space[0] if pos_slash<10 else self.Header[pos_slash-10]+10*self.Space[1],
                      '.': self.Header[pos_dot]+10*self.Space[0] if pos_dot<10 else self.Header[pos_dot-10]+10*self.Space[1]}
        i = 0
        for c in passphrase+'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if c not in self.Board:
                if c!=' ':
                    self.Board[c] = self.Header[i] if i<10 else self.Header[i-10]+10*self.Space[0] if i<20 else self.Header[i-20]+10*self.Space[1]
                i += 1
                while i==pos_slash+10 or i==pos_dot+10:
                    i += 1
        self.InvBoard = {self.Board[c]:c for c in self.Board}

    def print_board(self):
        print(''.join(map(str,self.Header)))
        print(''.join(self.InvBoard[self.Header[i]] if self.Header[i] in self.InvBoard else ' ' for i in range(10)))
        print(''.join(self.InvBoard[self.Header[i]+10*self.Space[0]] for i in range(10)))
        print(''.join(self.InvBoard[self.Header[i]+10*self.Space[1]] for i in range(10)))

    def encode(self, message, slash=True):
        C = []
        for c in message.upper():
            if 'A'<=c<='Z' or c=='.' or c=='/':
                C.append(self.Board[c])
            elif '0'<=c<='9':
                if slash:
                    C.append(self.Board['/'])
                C.append(c)
        return ''.join(map(str,C))

    def shift(self, C, key):
        return ''.join(str((int(c)+int(k))%10) for c,k in zip(C,cycle(key)))

    def inv_shift(self, C, key):
        return ''.join(str((int(c)-int(k))%10) for c,k in zip(C,cycle(key)))

    def decode(self, C, unslash=False):
        C = list(map(int,C))
        M = []
        second = slash = False
        for i in range(len(C)):
            if slash:
                M.append(str(C[i]))
                slash = False
            elif second:
                c = self.InvBoard[10*C[i-1]+C[i]]
                if unslash and c=='/':
                    slash = True
                else:
                    M.append(c)
                second = False
            else:
                if C[i] in self.InvBoard:
                    c = self.InvBoard[C[i]]
                    M.append(c)
                else:
                    second = True
        return ''.join(M)

    def encrypt(self, message, key):
        return self.decode(self.shift(self.encode(message),key))

    def decrypt(self, message, key):
        return self.decode(self.inv_shift(self.encode(message,False),key),True)


def main():
    encrypt = (input()=='1')
    header = input()
    passphrase = input()
    pos_slash,pos_dot = map(int,input().split())
    key = input()
    message = input()
    V = VIC(header, passphrase, pos_slash, pos_dot)
    #V.print_board()
    print(V.encrypt(message,key) if encrypt else V.decrypt(message,key))

main()
