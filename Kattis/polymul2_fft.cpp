#include <cstdio>
#include <vector>
using namespace std;
using ll = long long;

const ll MOD = 1004535809;
// phi(MOD) = MOD-1 = 2^21 * 479
const ll MOD2 = 740294657;
// phi(MOD) = MOD-1 = 2^21 * 353

ll power(ll a, ll b, ll MOD) {
  if (b==0) return 1;
  if ((b&1)==0) return power((a*a)%MOD,b>>1,MOD);
  return (a*power((a*a)%MOD,b>>1,MOD))%MOD;
}

// 3 is a primitive root mod MOD and MOD2
// 3^479 is of order 2^21 for MOD
const ll root = power(3,479,MOD);
const ll root_1 = power(root,MOD-2,MOD);  // inverse mod
const int root_pw = 1<<21;  // order
// 3^353 is of order 2^21 for MOD2
const ll root2 = power(3,353,MOD2);
const ll root_12 = power(root2,MOD2-2,MOD2);  // inverse mod
// these parameters allow us to compute the NTT mod MOD or MOD2
// of any sequence of size 2^k for k<=21

// modular FFT from e-maxx.ru/algo/fft_multiply
// https://www.hackerrank.com/contests/101hack46/challenges/counting-road-networks/editorial
void fft(ll MOD, ll root, ll root_1, int root_pw, vector<ll> &a, bool invert=false) {
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
    int nrev = power(n,MOD-2,MOD);  // inverse mod
    for (int i=0; i<n; ++i)
      a[i] = (a[i]*nrev)%MOD;
  }
}

const ll pq = MOD*MOD2;
const ll u = -170385281;  // bezout for MOD and MOD2
const ll v = 231202690;
const ll up = (((u*MOD)%pq)+pq)%pq;
const ll vq = (v*MOD2)%pq;

// integer overflow safe multiplication (slow)
ll mulmod(ll a, ll b, ll m=pq) {
  ll ab = 0;
  while (b) {
    if (b&1) {
      ab += a;
      if (ab>=m) ab -= m;
    }
    a = (a<<1)%m;
    b >>= 1;
  }
  return ab;
}

ll rev_chinois(ll a, ll b) {
  return (mulmod(b,up)+mulmod(a,vq))%pq;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t=0; t<T; ++t) {
    int N;
    scanf("%d", &N); ++N;
    vector<ll> A(N);
    for (int i=0; i<N; ++i) scanf("%lld", &A[i]);
    int M;
    scanf("%d", &M); ++M;
    vector<ll> B(M);
    for (int i=0; i<M; ++i) scanf("%lld", &B[i]);
    int n = 1;
    while (n<N || n<M) n <<= 1;
    n <<= 1;
    A.resize(n,0);
    B.resize(n,0);
    vector<ll> C = A, D = B;
    
    fft(MOD,root,root_1,root_pw,A);
    fft(MOD,root,root_1,root_pw,B);
    for (int i=0; i<n; ++i) A[i] = (A[i]*B[i])%MOD;
    fft(MOD,root,root_1,root_pw,A,true);
    
    fft(MOD2,root2,root_12,root_pw,C);
    fft(MOD2,root2,root_12,root_pw,D);
    for (int i=0; i<n; ++i) C[i] = (C[i]*D[i])%MOD2;
    fft(MOD2,root2,root_12,root_pw,C,true);
    
    for (int i=0; i<n; ++i) A[i] = rev_chinois(A[i],C[i]);
    while (A.size()>1 && A.back()==0) A.pop_back();
    int d = A.size() - 1;
    printf("%d\n", d);
    for (int i=0; i<=d; ++i)
      printf((i==d ? "%lld\n" : "%lld "), (A[i]<1LL<<31 ? A[i] : A[i]-MOD*MOD2));
  }
  return 0;
}
