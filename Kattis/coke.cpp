#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

/*
  Meaningful operations:
    10        ->  2*1
    10 + 3*1  ->  5
    2*5       ->  2*1
    5 + 3*1   ->  0
    8*1       ->  0
  Turns out we can completely ignore n1
  (provided we have enough).
*/

vector< vector< vector<int> > > Memo(151, vector< vector<int> >(151, vector<int>(51, -1)));

int dp(int c, int n5, int n10) {
  if (c<=0) return 0;
  if (Memo[c][n5][n10]<0) {
    int res = 8*c;
    if (n10>=1) {
      res = min(res, 1 + dp(c-1, n5, n10-1));
      res = min(res, 4 + dp(c-1, n5+1, n10-1));
    }
    if (n5>=2) res = min(res, 2 + dp(c-1, n5-2, n10));
    if (n5>=1) res = min(res, 4 + dp(c-1, n5-1, n10));
    Memo[c][n5][n10] = res;
  }
  return Memo[c][n5][n10];
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int C, n1, n5, n10;
    cin >> C >> n1 >> n5 >> n10;
    assert(n1 + 5*n5 + 10*n10 >= 8*C);
    cout << dp(C, n5, n10) << endl;
  }
  return 0;
}
