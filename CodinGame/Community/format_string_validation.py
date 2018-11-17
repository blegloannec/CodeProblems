#!/bin/bash

read -r S
read -r F
F=$(sed 's/[$\+*.|]/\\&/g;s/?/./g;s/~/.*/g' <<< "$F")
if grep -q "$F" <<< "$S"; then
    echo MATCH
else
    echo FAIL
fi
