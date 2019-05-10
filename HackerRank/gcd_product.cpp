#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

const ll MOD = 1000000007;

int N,M;
vector<ll> P;

void sieve() {
  vector<bool> Pr(N+1,true);
  for (int i=2; i<=N; ++i)
    if (Pr[i]) {
      P.push_back(i);
      for (int k=2*i; k<=N; k+=i)
	Pr[k] = false;
    }
}

ll expmod(ll x, ll n, ll m=MOD) {
  if (!n) return 1;
  if (!(n&1)) return expmod((x*x)%m,n>>1,m);
  return (x*expmod((x*x)%m,n>>1,m))%m;
}

int main() {
  cin >> N >> M;
  if (M>N) swap(N,M);
  sieve();
  ll res = 1;
  for (auto p : P) {
    ll q = p, e = 0;
    while (q<=M) {
      e += (N/q)*(M/q);
      q *= p;
    }
    res = (res * expmod(p,e)) % MOD;
  }
  cout << res << endl;
  return 0;
}
