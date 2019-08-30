tmp=_test_
for i in $(seq 5); do
    ./gen.py > "$tmp"
    a=$(python3 solution_naive.py < "$tmp")
    b=$(python3 solution_map.py < "$tmp")
    c=$(python3 solution.py < "$tmp")
    echo $a $b $c
    if [ $a -ne $b ] || [ $a -ne $c ] || [ $b -ne $c ]; then
	echo FAIL
	exit 1
    fi
done
rm "$tmp"
