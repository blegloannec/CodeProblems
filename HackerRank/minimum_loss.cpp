#include <iostream>
#include <vector>
#include <set>
using namespace std;

typedef long long ent;

int n;
vector<ent> P;

int main() {
  cin >> n;
  P.resize(n);
  for (int i=0; i<n; ++i) cin >> P[i];
  set<ent> S;
  ent res = 1LL<<62;
  for (int i=n-1; i>=0; --i) {
    auto it = S.insert(P[i]).first;
    if (it!=S.begin()) {
      --it;
      res = min(res,P[i]-*it);
    }
  }
  cout << res << endl;
  return 0;
}
