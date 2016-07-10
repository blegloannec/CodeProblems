#include <iostream>
#include <cstdlib>
using namespace std;

/*
  Generate pythagorean triples using Euclid's formula
  m>n
  a = m^2-n^2, b = 2mn, c = m^2+n^2
  prime triple <=> gcd(m,n) = 1 and m-n is odd
  a < b < c good triple <=> b-a | c
*/

const int N = 100000000;

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

int main() {
  long long cpt = 0L;
  for (int m=1; 2*m*m<N; ++m)
    for (int n=1+m%2; n<m; n+=2) {
      if (gcd(m,n)!=1) continue;
      int a = m*m-n*n;
      int b = 2*m*n;
      if (a==b) continue;
      int c = m*m+n*n;
      int l = a+b+c;
      if (c%abs(a-b)==0) cpt += N/l;
    }
  cout << cpt << endl;
  return 0;
}
