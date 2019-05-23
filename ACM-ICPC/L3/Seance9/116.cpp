#include <iostream>
#include <vector>
using namespace std;

int H, W;
vector< vector<int> > M, Pred;

int main() {
  while (cin >> H >> W) {
    M.resize(H);
    Pred.resize(H);
    for (int i=0; i<H; ++i) {
      M[i].resize(W);
      Pred[i].resize(W-1);
      for (int j=0; j<W; ++j) cin >> M[i][j];
    }
    for (int j=W-2; j>=0; --j)
      for (int i=0; i<H; ++i) {
	int vpred = 1<<30, ipred = H;
	for (int d=-1; d<=1; ++d) {
	  int i0 = (i+d+H) % H;
	  if (M[i0][j+1]<vpred || (M[i0][j+1]==vpred && i0<ipred)) {
	    vpred = M[i0][j+1];
	    ipred = i0;
	  }
	}
	M[i][j] += vpred;
	Pred[i][j] = ipred;
      }
    int imin = 0;
    for (int i=1; i<H; ++i)
      if (M[i][0]<M[imin][0]) imin = i;
    int i = imin, j = 0;
    cout << i+1;
    while (j<W-1) {
      i = Pred[i][j++];
      cout << ' ' << i+1;
    }
    cout << endl;
    cout << M[imin][0] << endl;
  }
  return 0;
}
