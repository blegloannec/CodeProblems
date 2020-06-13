#!/bin/bash

src="redblack avl stl treap splay ../skip_lists bst"
for f in $src; do
    g++ -O2 $f.cpp benchmark.cpp
    echo -e "$f    \t$(./a.out)"
    rm a.out
done
