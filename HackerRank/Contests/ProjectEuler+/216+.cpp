#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
using namespace std;

typedef long long ent;
const int N = 10000000;
vector<bool> P,PP;
vector<int> SPP;


// ===== GENERIC AUXILIARY CODE ===== //
ent expmod(ent x, ent n, ent m) {
  if (n==0) return 1;
  if ((n&1)==0) return expmod((x*x)%m,n>>1,m);
  return (x*expmod((x*x)%m,n>>1,m))%m;
}

int legendre(ent a, ent p) {
  // p an odd prime, a non 0
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
  while ((s&1)==0) {
    s >>= 1;
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

ent inv_mod(ent a, ent p) {  // p prime
  return expmod(a,p-2,p);
}

void prime_sieve(int N) {
  P.resize(N,true);
  P[0] = P[1] = false;
  for (int i=2; i*i<N; ++i)
    if (P[i])
      for (int k=2*i; k<N; k+=i)
	P[k] = false;
}


// ===== CODE SPECIFIC TO THE PROBLEM ===== //
vector<ent> solve(ent a, ent b, ent c, ent p) {
  vector<ent> sol;
  if (p==2) {
    if (c%2==0) sol.push_back(0);
    if ((a+b+c)%2==0) sol.push_back(1);
  }
  else {
    /*
      p an odd prime
      solve aX^2 + bX + c = 0 mod p
      D = b^2 - 4ac
      if D is a quadratic residue modulo p then
      for d^2 = D mod p, there exists 2 solutions
      x = (-b +/- d) * (2a)^(-1)  mod p
      as a in {1,2}, 2a is always invertible mod p
    */
    ent D = (((b*b - 4*a*c)%p)+p)%p;
    if (D==0)
      sol.push_back((((((-b)*inv_mod(2*a,p)))%p)+p)%p);
    else if (legendre(D,p)==1) {
      ent d = shanks_tonelli(D,p);
      ent inv_2a = inv_mod(2*a,p);
      sol.push_back(((((-b-d)*inv_2a)%p)+p)%p);
      sol.push_back(((((-b+d)*inv_2a)%p)+p)%p);
    }
  }
  return sol;
}

vector<ent> int_roots(ent a, ent b, ent c) {
  vector<ent> sol;
  ent D = b*b-4*a*c;
  if (D>=0) {
    ent d = (ent)sqrt(D);
    if (d*d==D) {
      if ((-b-d)%(2*a)==0) sol.push_back((-b-d)/(2*a));
      if ((-b+d)%(2*a)==0) sol.push_back((-b+d)/(2*a));
    }
  }
  return sol;
}

void trinomial_ad_hoc_sieve(ent a, ent b, ent c, int N) {
  int S = (int)sqrt((a*N+abs(b))*N+abs(c))+1;
  prime_sieve(S);
  PP.resize(N+1,true);
  // dealing with case P(n) = 1
  vector<ent> val1 = int_roots(a,b,c-1);
  for (auto iv=val1.begin(); iv!=val1.end(); ++iv)
    if (0<=*iv && *iv<=N) PP[*iv] = false;
  // dealing with case P(n) = -1
  val1 = int_roots(a,b,c+1);
  for (auto iv=val1.begin(); iv!=val1.end(); ++iv)
    if (0<=*iv && *iv<=N) PP[*iv] = false;
  // dealing with cases p | P(n) for p a prime
  for (ent p=2; p<S; ++p)
    if (P[p]) {
      vector<ent> sol = solve(a,b,c,p);
      for (auto ik=sol.begin(); ik!=sol.end(); ++ik) {
	ent k = *ik;
	while (k<=N) {
	  if ((a*k+b)*k+c!=p)  // do not mark primes themselves!
	    PP[k] = false;
	  k += p;
	}
      }
    }
  // prefix-sums
  SPP.resize(N+1,0);
  SPP[0] = (int)PP[0];
  for (int i=1; i<=N; ++i)
    SPP[i] = SPP[i-1] + (int)PP[i];
}


int main() {
  srand(time(NULL));
  ent a,b,c;
  cin >> a >> b >> c;
  trinomial_ad_hoc_sieve(a,b,c,N);
  int Q;
  cin >> Q;
  for (int q=0; q<Q; ++q) {
    int n;
    cin >> n;
    cout << SPP[n] << endl;
  }
  return 0;
}
