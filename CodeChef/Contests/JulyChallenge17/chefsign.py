#!/usr/bin/env python3

# plus longue chaine de < ou >
# en ignorant les =

def main():
    T = int(input())
    for _ in range(T):
        s = input()
        currC = None
        currL,maxL = 0,0
        for c in s:
            if c!='=':
                if c==currC:
                    currL += 1
                else:
                    currC = c
                    currL = 1
                maxL = max(currL,maxL)                
        print(maxL+1)

main()
