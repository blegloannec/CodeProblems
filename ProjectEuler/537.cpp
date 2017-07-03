#include <iostream>
#include <vector>
using namespace std;

/*
  Soit C(y) = nb de x tq pi(x) = y
  On a la relation de prog. dyn. suivante
  (choix de la valeur i pour pi() du dernier element)
  T(n,k) = sum( C(i)*T(n-i,k-1), 0<=i<=n )
  Donc en notant @ le produit de convolution (discrete)
  on a T(.,k) = C @ T(.,k-1)
  T(.,0) = 1,0,0,0,... le neutre pour @
  donc T(.,k) = C@^k pour @^ l'exponentiation de @
  @ se calcule en O(n log n) par FFT modulo (parfois
  appelee NTT = Number-Theoretic Transform)
  Donc en combinant FFT + exponentiation rapide
  on a un algo efficace en O(n log^2 n)
*/

typedef long long ll;

const int n = 20000;
const int N = 20*n;
vector<bool> P(N,true);
vector<ll> C(n+1,0);

void sieve() {
  P[0] = P[1] = false;
  for (int i=2; i*i<N; ++i)
    if (P[i])
      for (int k=2*i; k<N; k+=i)
	P[k] = false;
}

const ll MOD = 1004535809;
// phi(MOD) = MOD-1 = 2^21 * 479

ll power(ll a, int b) {
  if (b==0) return 1;
  if ((b&1)==0) return power((a*a)%MOD,b/2);
  return (a*power((a*a)%MOD,(b-1)/2))%MOD;
}

// 3 is a primitive root mod MOD
// hence 3^479 is of order 2^21
const ll root = power(3,479);
const ll root_1 = power(root,MOD-2);  // inverse mod
const int root_pw = 1<<21;  // order
// these parameters allow us to compute the NTT mod MOD
// of any sequence of size 2^k for k<=21

// modular FFT from e-maxx.ru/algo/fft_multiply
// https://www.hackerrank.com/contests/101hack46/challenges/counting-road-networks/editorial
void fft(vector<ll> &a, bool invert=false) {
  int n = a.size();
  // bit reverse ordering
  for (int i=1, j=0; i<n; ++i) {
    int bit = n >> 1;
    for (; j >= bit; bit>>=1) j -= bit;
    j += bit;
    if (i<j) swap(a[i],a[j]);
  }
  // efficient in-place iterative fft
  for (int len=2; len<=n; len<<=1) {
    ll wlen = invert ? root_1 : root;
    for (int i=len; i<root_pw; i<<=1)
      wlen = (wlen*wlen)%MOD;
    for (int i=0; i<n; i+=len) {
      ll w = 1;
      for (int j=0; j<len/2; ++j) {
	int u = a[i+j],  v = (a[i+j+len/2]*w)%MOD;
	a[i+j] = u+v < MOD ? u+v : u+v-MOD;
	a[i+j+len/2] = u-v >= 0 ? u-v : u-v+MOD;
	w = (w*wlen)%MOD;
      }
    }
  }
  if (invert) {
    int nrev = power(n,MOD-2);  // inverse mod
    for (int i=0; i<n; ++i)
      a[i] = (a[i]*nrev)%MOD;
  }
}

void convolve(vector<ll> &a, vector<ll> &b, vector<ll> &c) {
  vector<ll> ta = a, tb = b;
  int sz = a.size()<<1;
  ta.resize(sz,0);
  tb.resize(sz,0);
  c.resize(sz);
  fft(ta,false);
  fft(tb,false);
  for (int i=0; i<sz; ++i)
    c[i] = (ta[i]*tb[i])%MOD;
  fft(c,true);
}

void convolve_pow(vector<ll> &a, int b, vector<ll> &res) {
  if (b==0) {
    res.resize(a.size());
    fill(res.begin(),res.end(),0);
    res[0] = 1;
  }
  else {
    vector<ll> a2;
    convolve(a,a,a2);
    a2.resize(a.size());
    convolve_pow(a2,b/2,res);
    if (b&1) {
      convolve(a,res,res);
      res.resize(a.size());
    }
  }
}

int main() {
  sieve();
  int Pi = 0;
  int i = 1;
  while (Pi<=n) {
    if (P[i]) ++Pi;
    ++C[Pi];
    ++i;
  }
  int p2 = 1;
  while (p2<n+1) p2 <<= 1;
  C.resize(p2,0);
  vector<ll> res;
  convolve_pow(C,n,res);
  cout << res[n] << endl;
  return 0;
}
