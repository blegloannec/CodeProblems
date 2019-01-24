#!/bin/bash

read -r E
read -r T
read -r N
D=$(cat)

K=$(echo "$D" | head -1 | sed -E 's/:[[:alnum:]]*//g;s/,/\n/g' | cat -n | tr -d ' ' | tr '\t' ' ')
D=$(echo "$D" | sed -E 's/[[:alnum:]]*://g;s/,/ /g')
E=$(echo "$E" | sed -E 's/([+-])/\n\1 /g' | tail -n+2 | paste -d' ' - <(echo "$T" | tr ',' '\n'))

function gen_keys {
    while read -r o f t; do
        i=$(echo "$K" | egrep " $f$" | cut -d' ' -f1)
        printf " -k %d,%d" "$i" "$i"
        if [ "$t" = "int" ]; then printf "n"; fi
        if [ "$o" = "-" ]; then printf "r"; fi
    done
}

echo "$D" | sort $(echo "$E" | gen_keys) | cut -d' ' -f1
