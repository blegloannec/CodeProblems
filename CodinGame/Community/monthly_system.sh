#!/bin/bash

to_b12='s/Jan/0/g;s/Feb/1/g;s/Mar/2/g;s/Apr/3/g;s/May/4/g;s/Jun/5/g;s/Jul/6/g;s/Aug/7/g;s/Sep/8/g;s/Oct/9/g;s/Nov/A/g;s/Dec/B/g'
from_b12='s/A/Nov/g;s/B/Dec/g;s/0/Jan/g;s/1/Feb/g;s/2/Mar/g;s/3/Apr/g;s/4/May/g;s/5/Jun/g;s/6/Jul/g;s/7/Aug/g;s/8/Sep/g;s/9/Oct/g'

read N
S=0
for i in $(seq $N); do
    read M
    M=$(echo $M | sed $to_b12)
    S=$(echo "obase=12; ibase=12; $S+$M" | bc)
done
echo $S | sed $from_b12
