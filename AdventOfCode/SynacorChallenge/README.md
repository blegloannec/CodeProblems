# Synacor Challenge (2012)

[Synacor Challenge](https://challenge.synacor.com)

## Notes (spoilers!)

### Usage

```
$ python3 emulator.py challenge.bin
```

To replay some registered inputs at the beginning, then take the hand on the game, and logs inputs, use:
```
$ cat input_prefix - | tee input_log | python3 emulator.py challenge.bin
```

### Maze solver

The control command `*` solves the maze by a BFS in the emulator states.
```
$ cat maze - | python3 emulator.py challenge.bin
```

### Teleporter bypass

The control command `@` dumps a trace of every instruction executed while `&` modifies register 8 (see `emulator.py` source code for the associated bypass).

We dump the teleporter validation code:
```
$ cat teleporter - | python3 emulator.py challenge.bin
```
Let us sort out the dump a little:
```
$ sort trace.dump | uniq
```
And isolate the following important instructions:
```
05483   set R0 4
05486   set R1 1
05489   call 6027
05491   eq R1 R0 6
05495   jf R1 5579
(...)
06027   jt R0 6035
06030   add R0 R1 1
06034   ret
06035   jt R1 6048
06038   add R0 R0 32767
06042   set R1 R7
06045   call 6027
06047   ret
06048   push R0
06050   add R1 R1 32767
06054   call 6027
06056   set R1 R0
06059   pop R0
06061   add R0 R0 32767
06065   call 6027
06067   ret
```
The second part directly translates into the following code (where arithmetic operations are done on 15-bit unsigned int):
```
def f(R0=4, R1=1):
    if R0==0:
        return R1+1
    elif R1==0:
        return f(R0-1, R7)
    return f(R0-1, f(R0,R1-1))
```
Which is a variant of the [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function) (`R7 = 1` gives the standard Ackermann).
It is computed efficiently enough in `ack.cpp`.
