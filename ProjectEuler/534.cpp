#include <iostream>
#include <vector>
#include <map>
using namespace std;

/*
  backtracking + memoization
  runs in ~3 min with -O3
*/

typedef long long ll;
typedef vector<int> masks;
typedef vector< map<masks,ll> > memotbl;

// i the current line
// M the possible positions masks for each line >= i
ll Q(int n, int w, int i, masks &M, memotbl &memo) {
  if (i==n) return 1;
  if (memo[i].find(M)!=memo[i].end()) return memo[i][M];
  int full_mask = (1<<n)-1;
  ll res = 0;
  for (int a=0; a<n; ++a) {
    int A = 1<<a;
    if (!(M[0]&A)) {
      masks M0(++(M.begin()),M.end());
      bool skip = false;
      for (int d=1; d<=n-1-w && i+d<n; ++d) {
	M0[d-1] |= A;
	if (a+d<n) M0[d-1] |= A<<d;
	if (d<=a) M0[d-1] |= A>>d;
	if (M0[d-1]==full_mask) { // impossible conf
	  skip = true;
	  break;
	}
      }
      if (!skip) res += Q(n,w,i+1,M0,memo);
    }
  }
  memo[i][M] = res;
  return res;
}

ll S(int n) {
  // on a Q(n,n-1) = n^n
  ll res = n;
  for (int i=1; i<n; ++i) res *= n;
  for (int w=0; w<n-1; ++w) {
    masks M(n,0);
    memotbl memo(n);
    res += Q(n,w,0,M,memo);
  }
  return res;
}

int main() {
  cout << S(14) << endl;
  return 0;
}
