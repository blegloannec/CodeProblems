#!/bin/bash

function rotate {
    S=$(cat)
    W=$(echo "$S" | head -1 | tr -d '\n' | wc -c)
    for i in $(seq $W); do
        echo "$S" | cut -c $i | tr -d '\n'
        echo
    done
}

read H
S=$(cat)
if (echo "$S" | egrep -q '(\.\\|/\.|//|\\\\)') || (echo "$S" | rotate | egrep -q '(/\.|\\\.|//|\\\\)'); then
    echo -n UN
fi
echo STABLE
