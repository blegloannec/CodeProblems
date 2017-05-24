#include <iostream>
using namespace std;

typedef long long ll;

ll binom(ll n, ll p) {
  return p==0 ? 1 : n*binom(n-1,p-1)/p;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    ll n,k;
    cin >> n >> k;
    cout << binom(n-1,k-1) << endl;
  }
  return 0;
}
