/*
  for each p, we look for the acceptable n such that p | n^15 + 1
  i.e. n^15 = -1 [p]
  solutions are: a particular solution (-1) * each of the 15th primitive roots
  (or alternatively, for odd p, one in every two 30th primitive roots)

  runs in <20s with -O3
*/

#include <iostream>
#include <vector>
using namespace std;

typedef unsigned long long ent;
const int N = 100000000;
const ent M = 100000000001LL;

ent expmod(ent x, ent n, ent m) {
  if (!n) return 1;
  if (!(n&1)) return expmod((x*x)%m,n>>1,m);
  return (x*expmod((x*x)%m,n>>1,m))%m;
}

ent gcd(ent a, ent b) {
  return b==0?a:gcd(b,a%b);
}

vector<bool> P(N,true);
vector<int> F(N);
void sieve_smallest_factor() {
  P[0] = P[1] = false;
  for (int i=2; i<N; ++i)
    if (P[i]) {
      F[i] = i;
      for (int k=2*i; k<N; k+=i)
	if (P[k]) {
	  P[k] = false;
	  F[k] = i;
	}
    }
}

vector<int> factors(int n) {
  vector<int> D;
  while (n>1) {
    int p = F[n];
    D.push_back(p);
    do {n /= p;} while (n%p==0);
  }
  return D;
}

// x primitive root of p iff for each prime factor f of p-1, x^((p-1)/f) != 1
int primitive_root(int p) {
  vector<int> F = factors(p-1);
  for (unsigned int f=0; f<F.size(); ++f) F[f] = (p-1)/F[f];
  for (int i=2; i<p; ++i) {
    bool root = true;
    for (auto it=F.begin(); it!=F.end(); ++it)
      if (expmod(i,*it,p)==1) {
	root = false;
	break;
      }
    if (root) return i;
  }
  return 0;
}

int main() {
  sieve_smallest_factor();
  ent S = M-1;  // p = 2
  for (ent p=3; p<N; p+=2)
    if (P[p]) {
      ent r = primitive_root(p);
      ent g = gcd(p-1,15);
      ent y = expmod(r,(p-1)/g,p);  // primitive 15th root
      ent x = p-1;  // obvious particular solution to x^15 = -1
      // if there was no obvious solution, then the primitive 30th root
      // r^((p-1)/gcd(p-1,30)) would have worked as well (as p is odd,
      // p-1 is even, hence gcd(p-1,30) = 2*gcd(p-1,15) hence it cannot be
      // a 15th root)
      for (unsigned int i=0; i<g; ++i) {
	// there are g solutions to x^15 = -1, of the form x*y^k 
	S += p * (M/p + (x<M%p?1:0));
	x = (x*y)%p;
      }
    }
  cout << S << endl;
  return 0;
}
