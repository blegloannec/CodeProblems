#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef long long ent;

/*
  cf 407 & 451
  r is a fibonacci primitive root for p iff it is a primitive root
  ie is of order phi(p) = p-1 in (Z/pZ)*
  and r^n + r^(n+1) = r^(n+2) mod p for all n
  ie simply r^2 - r - 1 = 0 mod p
  the roots are (1 +/- sqrt(5) ) / 2
  there is a root if p>2 so that 2^(-1) exists and
  there exists s^2 = 5
  See: quadratic residue, Legendre symbol, Euler's criterion, Shanks-Tonelli
  quadratic residue law for 2 odd primes p and 5 gives
  (5|p)(p|5) = (-1)^(p-1) = 1 as p odd
  where (p|5) = [0,1,-1,-1,1][p%5]
  so that (5|p) = 1 iff p = 1 or 4 mod 5
  otherwise there is no sqrt(5) mod p and hence no solution
*/

const int N = 100000000;
vector<bool> P(N,true);
vector<int> F(N,1);

ent expmod(ent x, ent n, ent m) {
  if (n==0) return 1;
  if (n%2==0) return expmod((x*x)%m,n/2,m);
  return (x*expmod((x*x)%m,(n-1)/2,m))%m;
}

ent gcd(ent a, ent b) {
  return b==0?a:gcd(b,a%b);
}

int legendre(ent a, ent p) {
  // p an odd prime
  ent r = expmod(a,(p-1)/2,p);
  return r==p-1?-1:r;
}

ent random_non_residue(ent p) {
  ent a;
  do {a = rand()%p;} while (legendre(a,p)!=-1);
  return a;
}

ent shanks_tonelli(ent a, ent p) {
  // p and odd prime, a a quadratic residue
  // we assume legendre(a,p) == 1
  // returns a solution R, the other one will be -R mod p
  // factor p-1 = s*2^e with s odd
  ent s = p-1;
  int e = 0;
  while (s%2==0) {
    s /= 2;
    ++e;
  }
  // if e = 1, ie n = p mod 3, the solutions are +/- n^((p+1)/4)
  if (e==1) return expmod(a,(p+1)/4,p);
  // pick a non-residue (randomly, but could start with 2 and try incrementally)
  ent n = random_non_residue(p);
  ent x = expmod(a,(s+1)/2,p);
  ent b = expmod(a,s,p);
  ent g = expmod(n,s,p);
  int r = e;
  while (true) {
    ent t = b;
    int m = 0;
    while (t!=1) {
      t = (t*t)%p;
      ++m;
    }
    if (m==0) return x;
    ent gs = expmod(g,1L<<(r-m-1),p);
    g = (gs*gs)%p;
    x = (x*gs)%p;
    b = (b*g)%p;
    r = m;
  }
}

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

void factors(int n, vector<int> &D) {
  int p = F[n];
  D.push_back(p);
  do {n /= p;} while (n%p==0);
  if (n>1) factors(n,D);
}

ent bezout(ent a, ent b, ent &u, ent &v) {
  if (b==0) {
    u = 1;
    v = 0;
    return a;
  }
  ent u1,v1;
  ent g = bezout(b,a%b,u1,v1);
  u = v1;
  v = u1-(a/b)*v1;
  return g;
}

ent inv_mod(ent a, ent n) {
  ent u,v;
  bezout(a,n,u,v);
  return (u+n)%n;
}

/*
  If r is a primitive root of p, r as to be of order phi(p) = p-1 in
  (Z/pZ)* and it is sufficient to check whether r^((p-1)/f) != 1 mod p
  for each f prime factor of p-1.
*/
bool primitive_root(int r, int p, vector<int> &Dphi) {
  for (vector<int>::iterator it=Dphi.begin(); it!=Dphi.end(); ++it)
    if (expmod(r,(p-1)/(*it),p)==1) return false;
  return true;
}

bool fib_root(int p) {
  vector<int> Dphi;
  factors(p-1,Dphi);
  ent r5 = shanks_tonelli(5,p);
  ent i2 = inv_mod(2,p);
  return (primitive_root(((1+r5)*i2)%p,p,Dphi)||primitive_root(((1-r5+p)*i2)%p,p,Dphi));
}

int main() {
  srand(time(NULL));
  sieve_smallest_factor();
  ent S = 5; // for 5
  for (int p=7; p<N; p+=2)
    if (P[p] && (p%5==1 || p%5==4) && fib_root(p))
      S += p;
  cout << S << endl;
  return 0;
}
