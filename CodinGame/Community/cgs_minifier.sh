#!/bin/bash

function strip {
    str=0
    while IFS="" read -rn1 c; do
    	if [ "$c" = "'" ]; then
	    str=$((1-str))
    	fi
    	if [ $str -eq 1 ] || (echo "$c" | grep -q -v "[[:space:]]"); then
	    printf "%c" "$c"
    	fi
    done
}

function first_var {
    egrep -o '\$[[:alnum:]_]{2,}\$' | head -1 | sed 's/\$/\\\$/g'
}

function mini_vars {
    read -r S
    G=$(echo "$S" | first_var)
    i=97
    while [ -n "$G" ]; do
    	P=$(printf "s/$G/\$\x$(printf %x $i)\$/g")
    	S=$(echo "$S" | sed "$P")
    	i=$((i+1))
	G=$(echo "$S" | first_var)
    done
    echo "$S"
}

read N
strip | mini_vars
