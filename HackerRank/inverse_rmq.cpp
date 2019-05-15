#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>
using namespace std;

int N, M;
vector<int> A, RMQ;

void propagate(int i, int x) {
  while (i<M) {
    RMQ[i] = x;
    i = 2*i+1; // left child
  }
}

bool invRMQ() {
  int H = 0, n = N;
  while (n) {
    ++H;
    n >>= 1;
  }
  unordered_map<int,int> Count;
  for (auto a : A) ++Count[a];
  vector< set<int> > Lvl(H);
  for (auto x : Count) {
    if (x.second>H) return false;
    Lvl[x.second-1].insert(x.first);
  }
  RMQ.resize(M);
  // set the root
  if (Lvl[H-1].size()!=1) return false;
  propagate(0,*Lvl[H-1].begin());
  // set the other nodes, level by level, from top to bottom
  for (int h=H-2; h>=0; --h) {
    int k = 1<<(H-2-h);
    /* at level h, there are 2k nodes, the k even-indexed (right children)
       are missing, while the odd-indexed (left children) have been
       propagated from above */
    if ((int)Lvl[h].size()!=k) return false;
    for (int i=0; i<k; ++i) {
      int j = 2*(k+i);
      /* the unknown RMQ[j] (right child) has to be greater than the
	 known RMQ[j-1] (left child and father's value by construction)
	 we binary search for the best available */
      auto it = Lvl[h].lower_bound(RMQ[j-1]);
      if (it==Lvl[h].end()) return false;
      propagate(j,*it);
      Lvl[h].erase(it);
    }
  }
  return true;
}

int main() {
  cin >> N;
  M = 2*N-1;
  A.resize(M);
  for (int i=0; i<M; ++i) cin >> A[i];
  if (invRMQ()) {
    cout << "YES\n";
    for (int i=0; i<M; ++i)
      cout << RMQ[i] << (i==M-1 ? '\n' : ' ');
  }
  else cout << "NO\n";
  return 0;
}
