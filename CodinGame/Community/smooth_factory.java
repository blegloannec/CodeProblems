import java.util.*;
import java.io.*;
import java.math.*;
import java.util.function.*;
import java.util.stream.*;

class HammingGen {
    private long Factors[] = {2L,3L,5L};
    private TreeSet<Long> S = new TreeSet<>();
    
    public HammingGen() {
        S.add(1L);
    }
    
    public long next() {
        long x = S.pollFirst();
        for (long d : Factors) S.add(d*x);
        return x;
    }
    
    public Stream<Long> stream() {
        return Stream.generate(() -> next());
    }
}

class Solution {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int V = in.nextInt();
        HammingGen H = new HammingGen();
        System.out.println(H.stream().limit(V).mapToLong(i->i).sum());
    }
}
