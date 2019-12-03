#include <iostream>
#include <vector>
using namespace std;

int main() {
  int B,T;
  cin >> B;
  vector<int> V(B);
  for (int i=0; i<B; ++i) cin >> V[i];
  cin >> T;
  vector<int> FarmMask(T,0);
  for (int i=0; i<T; ++i) {
    int M;
    cin >> M;
    for (int j=0; j<M; ++j) {
      int t;
      cin >> t; --t;
      FarmMask[i] |= 1<<t;
    }
  }
  // O(2^B * (T+B))
  int res = 0;
  for (int mask=0; mask<(1<<B); ++mask) {
    bool inter = true;
    for (int farm : FarmMask)
      if ((farm&mask)==0) {
	inter = false;
	break;
      }
    if (inter) {
      // the bean set intersects all the farms, it is a valid final set
      // we compute the cost of its complementary
      int cost = 0;
      for (int i=0; i<B; ++i)
	if (((mask>>i)&1)==0) cost += V[i];
      res = max(res, cost);
    }
  }
  cout << res << endl;
  return 0;
}
