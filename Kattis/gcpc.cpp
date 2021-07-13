#include <iostream>
#include <vector>
#include <set>
using namespace std;

struct team {
  int t, prb, pen;
  team(int t) : t(t), prb(0), pen(0) {}
  bool operator<(const team &B) const {  // /!\ non-total (t unused)
    return prb<B.prb || (prb==B.prb && pen>B.pen);
  }
};

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int N, M;
  cin >> N >> M;
  vector<team> T;
  for (int t=0; t<N; ++t) T.push_back(team(t));
  multiset<team> Better;
  // as we use a non-total <, we keep pointers to elements
  vector< multiset<team>::iterator > Node(N, Better.end());
  for (int i=0; i<M; ++i) {
    int t,p;
    cin >> t >> p; --t;
    if (t>0) {
      if (Node[t]!=Better.end()) {
	Better.erase(Node[t]);
	Node[t] = Better.end();
      }
      T[t].prb += 1;
      T[t].pen += p;
      if (T[0]<T[t])
	Node[t] = Better.insert(T[t]);
    }
    else {
      T[0].prb += 1;
      T[0].pen += p;
      while (!(Better.empty() || T[0]<*Better.begin())) {
	Node[Better.begin()->t] = Better.end();
	Better.erase(Better.begin());
      }
    }
    cout << Better.size()+1 << '\n';
  }
  return 0;
}
