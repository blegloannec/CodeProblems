#include <iostream>
#include <vector>
using namespace std;

const int inf = 1<<30;

int main() {
  int cas;
  cin >> cas;
  while (cas--) {
    int W,H;
    cin >> W >> H;
    vector< vector<int> > DP(H);
    int res = 0;
    for (int i=0; i<H; ++i) {
      DP[i].resize(W,inf);
      // permier/dernier pair de la ligne
      int l = -1, r = -1;  
      for (int j=0; j<W; ++j) {
	char c;
	cin >> c;
	int d = c-'0';
	if (d%2==0) {
	  if (l<0) l = j;
	  r = j;
	}
      }
      // prog. dyn. des distances
      // DP[i][j] la distance min pour atteindre (i,j) en ayant
      // visite tous les pairs des lignes <=i
      if (i==0)  // init. de la premiere ligne
	for (int j=0; j<W; ++j) {
	  if (l>=0)
	    DP[0][j] = min(l + (r-l) + abs(j-r),
			   r + (r-l) + abs(j-l));
	  else
	    DP[0][j] = j;
	}
      else  // cas general
	for (int j=0; j<W; ++j)
	  // j0 la position d'ou l'on descend de la ligne precedente
	  for (int j0=0; j0<W; ++j0) {
	    if (l>=0)
	      // chemins j0 -> l -> r -> j ou j0 -> r -> l -> j
	      DP[i][j] = min(DP[i][j],
			     min(DP[i-1][j0]+1 + abs(l-j0) + (r-l) + abs(j-r),
				 DP[i-1][j0]+1 + abs(r-j0) + (r-l) + abs(j-l)));
	    else
	      DP[i][j] = min(DP[i][j], DP[i-1][j0]+1 + abs(j-j0));
	  }
      if (l>=0) {
	res = inf;
	for (int j=0; j<W; ++j) res = min(res,DP[i][j]);
      }
    }
    cout << res << endl;
  }
  return 0;
}
