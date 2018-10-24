#include <iostream>
#include <vector>
using namespace std;

/*
  O(H*W*DMAX) = O(H*W*(H+W)) = O(N^3) for N = H+W
  instead of O(N^4) for the naive approach

  O-------------------O'
  |          1   1B   |
  |   1               |
  |   1      1A       |
  |                   |

  any pair of 1 is "seen" from one exactly origin O or O'
  (e.g. that for (A,B), the dist(A,B) = dist(O',A) - dist(O',B))
  except for pairs horizontally or vertically aligned that
  are seen twice
*/

int H,W,DMAX;
vector<string> G;
vector< vector< vector<int> > > D;

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> H >> W;
    G.resize(H);
    for (int i=0; i<H; ++i) cin >> G[i];
    DMAX = H+W-1;
    vector<int> Cnt(DMAX,0);  // result vector
    /* for O = (0,0) the origin
       D[i][j][d] = nb of points (x,y) with x<=i and y<=j
                    that are at distance d from the origin */
    D.resize(H); 
    for (int i=0; i<H; ++i) {
      D[i].resize(W);
      for (int j=0; j<W; ++j) {
	// we copy the distance vector from (i,j-1)
	if (j==0) D[i][j].resize(DMAX,0);
	else D[i][j] = D[i][j-1];
	// we complete the j column
	for (int k=0; k<=i; ++k)
	  if (G[k][j]=='1') ++D[i][j][k+j];
	if (G[i][j]=='1')
	  /* we add pairs involving (i,j) and any (a,b) with
	     a<=i and b<=j to the count */
	  for (int d=0; d<i+j; ++d) Cnt[i+j-d] += D[i][j][d];
      }
    }
    // same with O' = (0,W-1) as the origin
    D.clear();
    D.resize(H); 
    for (int i=0; i<H; ++i) {
      D[i].resize(W);
      for (int j=W-1; j>=0; --j) {
	if (j==W-1) D[i][j].resize(DMAX,0);
	else D[i][j] = D[i][j+1];
	for (int k=0; k<=i; ++k)
	  if (G[k][j]=='1') ++D[i][j][k+W-1-j];
	if (i>0 && j<W-1 && G[i][j]=='1')
	  /* we add pairs involving (i,j) and any (a,b) with
	     a<i and b>j to the count */
	  for (int d=0; d<i+W-1-j; ++d) Cnt[i+W-1-j-d] += D[i-1][j+1][d];
      }
    }
    for (int d=1; d<DMAX; ++d)
      cout << Cnt[d] << (d==DMAX-1 ? '\n' : ' ');
    D.clear(); 
  }
  return 0;
}
