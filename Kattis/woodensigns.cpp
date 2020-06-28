#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

const ll MOD = (1LL<<31)-1LL;

int N;
vector<int> P;
vector< vector<int> > Memo;

// O(N^2) DP
// count(i, p) = nb of conf. of arrows >=i with arrow i starting at pos. p
int count(int i, int p0) {
  if (i==N) return 1;
  int *memo = &Memo[i][p0];  // because p0 might be swapped below...
  if (*memo<0) {
    int p1 = P[i];    // current head
    if (p1<p0) swap(p0, p1);
    int q1 = P[i+1];  // next head
    ll res = 0;
    if (p0<q1) res += count(i+1, p0);
    if (q1<p1) res += count(i+1, p1);
    *memo = res % MOD;
  }
  return *memo;
}

int main() {
  cin >> N;
  P.resize(N+1);
  for (int i=0; i<N+1; ++i) cin >> P[i];
  Memo.resize(N+1, vector<int>(N+2,-1));
  cout << count(1, P[0]) << endl;
  return 0;
}
