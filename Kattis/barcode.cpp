#include <iostream>
//#include <cassert>
using namespace std;
using ll = long long;

ll mul(ll a, ll b, ll m) {
  a *= b;
  if (a>=m) a %= m;
  return a;
}

ll expmod(ll x, ll n, ll m) {
  if (n==0) return 1;
  if ((n&1)==0) return expmod(mul(x,x,m),n>>1,m);
  return mul(x,expmod(mul(x,x,m),n>>1,m),m);
}

ll invmod(ll x, ll p) {  // slow, call as few as possible
  return expmod(x%p, p-2, p);
}

ll binommod_aux(ll n, ll p, ll m) {
  //assert(n<m);
  if (p>n) return 0;
  ll res = 1, res_inv = 1;
  for (ll i=0; i<p; ++i) {
    res = mul(res, n-i, m);
    res_inv = mul(res_inv, p-i, m);
  }
  return mul(res, invmod(res_inv,m),m);
}

ll binommod(ll n, ll p, ll m) {  // using lucas' thm
  //assert(0<=p && p<=n);
  ll res = 1;
  while (n) {
    res = mul(res, binommod_aux(n%m,p%m,m), m);
    n /= m;
    p /= m;
  }
  return res;
}

ll barcode(ll N, ll M) {
  // no two consecutive 1 -> fibonacci
  ll F0 = 1, F1 = 2%M;
  for (int i=2; i<=N; ++i) {
    ll svg = F1;
    F1 += F0;
    if (F1>=M) F1 -= M;
    F0 = svg;
  }
  /* if N is even, we can have the same nb of 1 and 0
     in that case, there are binom(N,N/2) such words
     the 2 words (01)^(N/2) and (10)^(N/2) are already in F1
     as well as the N/2-1 words of the form:
     10101..1001..101 with exactly 1 double 0 somewhere */
  if (N%2==0)
    F1 = (F1 + binommod(N,N/2,M) - 2 - (N/2-1)) % M;
  if (F1<0) F1 += M;
  return F1;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    ll N,M;
    cin >> N >> M;
    cout << barcode(N,M) << endl;
  }
  return 0;
}
