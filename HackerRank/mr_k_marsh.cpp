#include <iostream>
#include <vector>
using namespace std;

// O(n^2 m) similar to largest rectangle of 1 in a grid of 0/1

int main() {
  int m,n;
  cin >> m >> n;
  vector<string> G(m);
  for (int i=0; i<m; ++i) cin >> G[i];
  vector< vector<int> > CX(m);
  for (int i=0; i<m; ++i) {
    CX[i].resize(n);
    for (int j=0; j<n; ++j) {
      CX[i][j] = G[i][j]=='x' ? 1 : 0;
      if (j>0) CX[i][j] += CX[i][j-1];
    }
  }
  int pmax = 0;
  for (int l=0; l<n; ++l) {
    for (int r=l+1; r<n; ++r) {
      int i0 = -1;
      for (int i=0; i<m; ++i) {
	int nx = CX[i][r] - (l>0 ? CX[i][l-1] : 0);
	if (nx==0) {
	  if (i0<0) i0 = i;
	  else pmax = max(pmax,2*(i-i0+r-l));
	}
	else if (G[i][l]=='x' || G[i][r]=='x') i0 = -1;
      }
    }
  }
  if (pmax==0) cout << "impossible" << endl;
  else cout << pmax << endl;
  return 0;
}
