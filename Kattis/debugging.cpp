#include <iostream>
#include <vector>
#include <climits>
using namespace std;
using ll = long long;

ll r,p;
vector<ll> Memo;

ll dp(int n) {
  if (Memo[n]<0) {
    ll res = LLONG_MAX;
    for (int k=1; k<=n; ++k)
      res = min(res, r+k*p+dp((n+k)/(k+1)));
    Memo[n] = res;
  }
  return Memo[n];
}

int main() {
  int n;
  cin >> n >> r >> p;
  Memo.resize(n+1,-1);
  Memo[0] = Memo[1] = 0;
  cout << dp(n) << endl;
  return 0;
}
