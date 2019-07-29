import java.util.*;
import java.io.*;
import java.math.*;

class Complex {
    public double a, b;
    
    public Complex(double re, double im) {
        a = re; b = im;
    }
    
    public Complex(String s) {
        int i = s.indexOf('+');
        if (i<0) i = s.lastIndexOf('-');
        a = Double.parseDouble(s.substring(0,i));
        b = Double.parseDouble(s.substring(i,s.length()-1));
    }
    
    public double abs() {
        return Math.hypot(a, b);
    }
    
    public Complex add(Complex z) {
        return new Complex(a+z.a, b+z.b);
    }
    
    public Complex mul(Complex z) {
        return new Complex(a*z.a-b*z.b, a*z.b+b*z.a);
    }
}

class Solution {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        String sc = in.nextLine();
        Complex c = new Complex(sc);
        int m = in.nextInt();
        Complex z = new Complex(0.,0.);
        int i = 0;
        while (z.abs()<2. && ++i<m) z = z.mul(z).add(c);
        System.out.println(i);
    }
}
