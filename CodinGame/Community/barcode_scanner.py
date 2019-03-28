#!/usr/bin/env python3

Codes = {'0001101': 'L0', '0100111': 'G0', '1110010': 'R0',
         '0011001': 'L1', '0110011': 'G1', '1100110': 'R1',
         '0010011': 'L2', '0011011': 'G2', '1101100': 'R2',
         '0111101': 'L3', '0100001': 'G3', '1000010': 'R3',
         '0100011': 'L4', '0011101': 'G4', '1011100': 'R4',
         '0110001': 'L5', '0111001': 'G5', '1001110': 'R5',
         '0101111': 'L6', '0000101': 'G6', '1010000': 'R6',
         '0111011': 'L7', '0010001': 'G7', '1000100': 'R7',
         '0110111': 'L8', '0001001': 'G8', '1001000': 'R8',
         '0001011': 'L9', '0010111': 'G9', '1110100': 'R9'}

First = {'LLLLLLRRRRRR': '0', 'LLGLGGRRRRRR': '1', 'LLGGLGRRRRRR': '2', 'LLGGGLRRRRRR': '3', 'LGLLGGRRRRRR': '4',
         'LGGLLGRRRRRR': '5', 'LGGGLLRRRRRR': '6', 'LGLGLGRRRRRR': '7', 'LGLGGLRRRRRR': '8', 'LGGLGLRRRRRR': '9'}

def decode_part(part):
    depart = tuple(Codes[part[i:i+7]] for i in range(0,42,7))
    pattern, code = (''.join(C) for C in zip(*depart))
    return code, pattern

def debarcode(barcode):
    assert len(barcode)==95
    left_guard = barcode[:3]
    assert left_guard=='101'
    left_part = barcode[3:45]
    central_guard = barcode[45:50]
    assert central_guard=='01010'
    right_part = barcode[50:92]
    right_guard = barcode[92:]
    assert right_guard=='101'
    left_code, left_pattern = decode_part(left_part)
    right_code, right_pattern = decode_part(right_part)
    pattern = left_pattern + right_pattern
    code = First[pattern] + left_code + right_code
    checksum = sum(int(code[i]) for i in range(0,13,2)) + 3*sum(int(code[i]) for i in range(1,13,2))
    assert checksum%10==0
    return code

if __name__=='__main__':
    scanline = input()
    try:
        try:
            print(debarcode(scanline))
        except:
            print(debarcode(scanline[::-1]))
    except:
        print('INVALID SCAN')
