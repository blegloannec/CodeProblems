#!/usr/bin/env python3

import sys

class Packet:
    ID_SUM, ID_PROD, ID_MIN, ID_MAX, ID_LITERAL, ID_GT, ID_LT, ID_EQ = range(8)

    def __init__(self, B, i=0):
        self.lidx = i
        self.version = int(B[i:i+3], 2)
        i += 3
        self.type_id = int(B[i:i+3], 2)
        i += 3
        if self.type_id==self.ID_LITERAL:
            Lit = []
            while True:
                grp = B[i:i+5]
                Lit.append(grp[1:])
                i += 5
                if grp[0]=='0':
                    break
            self.literal = int(''.join(Lit), 2)
        else:
            self.length_id = int(B[i], 2)
            i += 1
            self.Sub = []
            if self.length_id==0:
                self.sub_len = int(B[i:i+15], 2)
                i += 15
                i0 = i
                while i < i0+self.sub_len:
                    self.Sub.append(Packet(B, i))
                    i = self.Sub[-1].ridx
                assert i == i0+self.sub_len
            else:
                self.sub_cnt = int(B[i:i+11], 2)
                i += 11
                while len(self.Sub) < self.sub_cnt:
                    self.Sub.append(Packet(B, i))
                    i = self.Sub[-1].ridx
        self.ridx = i

    def version_sum(self):
        res = self.version
        if self.type_id!=self.ID_LITERAL:
            for sub in self.Sub:
                res += sub.version_sum()
        return res

    def value(self):
        if self.type_id==self.ID_LITERAL:
            return self.literal
        elif self.type_id==self.ID_SUM:
            return sum(sub.value() for sub in self.Sub)
        elif self.type_id==self.ID_PROD:
            v = 1
            for sub in self.Sub:
                v *= sub.value()
            return v
        elif self.type_id==self.ID_MIN:
            assert self.Sub
            return min(sub.value() for sub in self.Sub)
        elif self.type_id==self.ID_MAX:
            assert self.Sub
            return max(sub.value() for sub in self.Sub)
        elif self.type_id==self.ID_GT:
            assert len(self.Sub)==2
            return 1 if self.Sub[0].value()>self.Sub[1].value() else 0
        elif self.type_id==self.ID_LT:
            assert len(self.Sub)==2
            return 1 if self.Sub[0].value()<self.Sub[1].value() else 0
        elif self.type_id==self.ID_EQ:
            assert len(self.Sub)==2
            return 1 if self.Sub[0].value()==self.Sub[1].value() else 0
        assert False, f'Unknown type ID: {self.type_id}'

    def __repr__(self):
        return f'<{self.version} {self.type_id} {self.literal if self.type_id==self.ID_LITERAL else self.Sub}>'


if __name__=='__main__':
    for L in sys.stdin.readlines():
        HI = L.strip()
        BI = ''.join(f'{int(h,16):04b}' for h in HI)
        P = Packet(BI)
        print(P.version_sum(), P.value())
