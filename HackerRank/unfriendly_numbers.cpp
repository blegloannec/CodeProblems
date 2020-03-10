#include <cstdio>
#include <vector>
#include <unordered_set>
using namespace std;
using ll = long long;

ll gcd(ll a, ll b) {
  return b==0 ? a : gcd(b, a%b);
}

ll decomp(ll n, vector<ll> &Factors) {
  ll div_cnt = 1;
  int m = 0;
  while ((n&1)==0) {
    n >>= 1;
    ++m;
  }
  if (m>0) {
    Factors.push_back(2);
    div_cnt *= m+1;
  }
  ll d = 3;
  while (d*d<=n) {
    m = 0;
    while (n%d==0) {
      n /= d;
      ++m;
    }
    if (m>0) {
      Factors.push_back(d);
      div_cnt *= m+1;
    }
    d += 2;
  }
  if (n>1) {
    Factors.push_back(n);
    div_cnt *= 2;
  }
  return div_cnt;
}

int main() {
  int n; ll f;
  scanf("%d %lld", &n, &f);
  unordered_set<ll> Div;
  for (int i=0; i<n; ++i) {
    ll u;
    scanf("%lld", &u);
    Div.insert(gcd(u, f));
  }
  vector<ll> Factors;
  ll div_cnt = decomp(f, Factors);
  vector<ll> Q(Div.begin(), Div.end());
  while (!Q.empty()) {
    ll d = Q.back();
    Q.pop_back();
    for (ll p : Factors)
      if (d%p==0) {
	ll d0 = d/p;
	if (Div.find(d0)==Div.end()) {
	  Q.push_back(d0);
	  Div.insert(d0);
	}
      }
  }
  div_cnt -= Div.size();
  printf("%lld\n", div_cnt);
  return 0;
}
