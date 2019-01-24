#!/bin/bash

read -r N
read -r M
P=$(head -$N)
V=$(cat)

function compte {
    Yes=0
    No=0
    while read -r p n; do
        v=$(echo "$V" | egrep "^$p ")
        m=$(echo "$v" | wc -l)
        if [ "$n" -ge "$m" ]; then
            Yes=$(( Yes + $(echo "$v" | egrep -c " Yes$") ))
            No=$(( No + $(echo "$v" | egrep -c " No$") ))
        fi
    done
    echo "$Yes $No"
}

echo "$P" | compte
