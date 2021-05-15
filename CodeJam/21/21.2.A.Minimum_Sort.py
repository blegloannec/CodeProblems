#!/usr/bin/env python3

# basic selection sort
# costs exactly sum((10**8+i-1)//i for i in range(2, 101)) = 418737795 < 6e8
def case():
    for i in range(1, N):
        print(f'M {i} {N}', flush=True)
        k = int(input())
        if i<k:
            print(f'S {i} {k}', flush=True)
            assert input()=='1'
    print('D', flush=True)
    assert input()=='1'

def main():
    global N
    T,N = map(int, input().split())
    for _ in range(T):
        case()

main()
