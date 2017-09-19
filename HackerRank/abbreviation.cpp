#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

bool is_upper(char c) {
  return ('A'<=c && c<='Z');
}

char to_upper(char c) {
  assert('a'<=c && c<='z');
  return 'A'+(c-'a');
}

bool dp(string &A, string &B) {
  int n = A.size(), m = B.size();
  vector< vector<bool> > T(n+1);
  for (int i=0; i<=n; ++i) T[i].resize(m+1,false);
  T[0][0] = true;
  for (int i=1; i<=n; ++i)
    for (int j=0; j<=m; ++j) {
      if (is_upper(A[i-1]))
	T[i][j] = (j>0 && A[i-1]==B[j-1] ? T[i-1][j-1] : false);
      else {
	T[i][j] = T[i-1][j];
	if (!T[i][j] && j>0 && to_upper(A[i-1])==B[j-1]) T[i][j] = T[i-1][j-1];
      }
    }
  return T[n][m];
}

int main() {
  int q;
  cin >> q;
  for (int t=0; t<q; ++t) {
    string a,b;
    cin >> a >> b;
    cout << (dp(a,b) ? "YES" : "NO") << endl;
  }
  return 0;
}
