#include <iostream>
#include <vector>
using namespace std;

int W,H;
vector< vector<int> > G;

// O(W^2 H) similar to largest rectangle of 1 in a grid of 0/1
int max_sum_rect() {
  vector< vector<int> > CX = G;
  for (int i=0; i<H; ++i)
    for (int j=1; j<W; ++j)
      CX[i][j] += CX[i][j-1];
  int res = -1000000;
  for (int l=0; l<W; ++l)
    for (int r=l; r<W; ++r) {
      int s = 0;
      for (int i=0; i<H; ++i) {
	int nx = CX[i][r] - (l>0 ? CX[i][l-1] : 0);
	s = max(s+nx,nx);
	res = max(res,s);
      }
    }
  return res;
}

int main() {
  cin >> W >> H;
  G.resize(H);
  for (int i=0; i<H; ++i) {
    G[i].resize(W);
    for (int j=0; j<W; ++j) cin >> G[i][j];
  }
  cout << max_sum_rect() << endl;
  return 0;
}
