#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define _t_ first
#define _l_ second

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int N,K;
  cin >> N >> K;
  vector< pair<int,bool> > I;
  for (int i=0; i<N; ++i) {
    int l,r;
    cin >> l >> r;
    I.push_back(make_pair(l, true));
    I.push_back(make_pair(r, false));
  }
  sort(I.begin(), I.end());
  N *= 2;
  int j = 0, cnt = 0, res = 0;
  for (int i=0; i<N; ++i) {
    while (j<N && I[j]._t_-I[i]._t_<=K) {
      if (I[j]._l_) ++cnt;
      res = max(res, cnt);
      ++j;
    }
    if (!I[i]._l_) --cnt;
  }
  cout << res << endl;
  return 0;
}
