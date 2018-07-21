#include <iostream>
using namespace std;

typedef long long ent;

/*
  Somehow harder version of problem 39
  Generate pythagorean triples using Euclid's formula
  m>n
  a = m^2-n^2, b = 2mn, c = m^2+n^2
  prime triple <=> gcd(m,n) = 1 and m-n is odd
*/

const int N = 1500001;
int cpt[N];

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

int main() {
  for (int n=0; n<N; ++n) cpt[n] = 0;
  for (int m=1; 2*m*m<N; ++m) {
    for (int n=1+m%2; n<m; n+=2) {
      if (gcd(m,n)!=1) continue;
      int l = 2*m*m+2*m*n;
      for (int k=l; k<N; k+=l) ++cpt[k];
    }
  }
  int res = 0;
  for (int n=2; n<N; ++n)
    if (cpt[n]==1) ++res;
  cout << res << endl;
  return 0;
}
