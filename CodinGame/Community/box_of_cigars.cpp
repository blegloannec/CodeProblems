#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> L(N);
  for (int i=0; i<N; ++i) cin >> L[i];
  vector< unordered_map<int,int> > DP(N);
  int res = 0;
  for (int i=1; i<N; ++i)
    for (int j=0; j<i; ++j) {
      int d = L[i]-L[j];
      DP[i][d] = DP[j][d]+1;
      res = max(res, DP[i][d]);
    }
  cout << ++res << endl;
  return 0;
}
