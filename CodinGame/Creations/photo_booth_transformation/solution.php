<?php

function gcd($a, $b) {
    return $b==0 ? $a : gcd($b, $a%$b);
}

function lcm($a, $b) {
    return intdiv($a*$b, gcd($a, $b));
}

function photobooth($w, $h, $x, $y) {
    return array(($x>>1)+($x&1)*($w>>1), ($y>>1)+($y&1)*($h>>1));
}

// period of a permutation = LCM of the sizes of its cycles
function permutation_period($P) {
    $size = sizeof($P);
    $period = 1;
    $Seen = array_fill(0, $size, false);
    for ($i=0; $i<$size; ++$i) {
        if (!$Seen[$i]) {
            $j = $i;
            $c = 0;
            while (!$Seen[$j]) {
                $Seen[$j] = true;
                ++$c;
                $j = $P[$j];
            }
            $period = lcm($period, $c);
        }
    }
    return $period;
}

// O(w*h) approach (expected)
function solution2d($w, $h) {
    $P = array();
    for ($x=0; $x<$w; ++$x) {
        for ($y=0; $y<$h; ++$y) {
            list($x1,$y1) = photobooth($w, $h, $x, $y);
            $P[$x*$h + $y] = $x1*$h + $y1;
        }
    }
    return permutation_period($P);
}

// O(w+h) approach noticing both dimensions are independent
function solution1d($w, $h) {
    $Px = array();
    for ($x=0; $x<$w; ++$x) $Px[$x] = photobooth($w, $h, $x, 0)[0];
    $Py = array();
    for ($y=0; $y<$h; ++$y) $Py[$y] = photobooth($w, $h, 0, $y)[1];
    return lcm(permutation_period($Px), permutation_period($Py));
}

/*
  There is also a "formula" for the period of the 1d-permutations
  (period on one dimension w = multiplicative order of 2 mod w-1)
  - ad-hoc proof (in French):
    https://fr.wikipedia.org/wiki/Transformation_du_clich%C3%A9_Photomaton
  - or notice the 1d-perm. is the inverse of a classic cards "faro shuffle":
    https://en.wikipedia.org/wiki/Faro_shuffle
*/
function solution_formula($w, $h) {
    $l = 1;
    foreach (array($w-1, $h-1) as $d) {
        if ($d>1) {
            // multiplicative order of 2 mod d (odd), computed "naively"
            $k = 2;
            $p = 1;
            while ($k!=1) {
                $k = (2*$k) % $d;
                ++$p;
            }
            $l = lcm($l, $p);
        }
    }
    return $l;
}

function main() {
    fscanf(STDIN, "%d", $T);
    for ($t=0; $t<$T; ++$t) {
        fscanf(STDIN, "%d %d", $w, $h);
        $res = solution2d($w, $h);
        //$res = solution1d($w, $h);
        //$res = solution_formula($w, $h);
        echo("$res\n");
    }
}

main();

?>