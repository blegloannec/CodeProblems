#include <iostream>
#include <vector>
using namespace std;

int n;
vector< vector<bool> > G;
vector< vector<int> > W;

void floyd_warshall() {
  for (int k=0; k<n; ++k)
    for (int u=0; u<n; ++u)
      if (G[u][k])
	for (int v=0; v<n; ++v)
	  if (G[k][v]) {
	    if (G[u][v])
	      W[u][v] = min(W[u][v], W[u][k]+W[k][v]);
	    else {
	      G[u][v] = true;
	      W[u][v] = W[u][k]+W[k][v];
	    }
	  }
}

int main() {
  int m;
  cin >> n >> m;
  G.resize(n, vector<bool>(n,false));
  W.resize(n, vector<int>(n,0));
  for (int i=0; i<n; ++i) G[i][i] = true;
  for (int i=0; i<m; ++i) {
    int x,y,r;
    cin >> x >> y >> r; --x; --y;
    G[x][y] = true;
    W[x][y] = r;
  }
  floyd_warshall();
  int q;
  cin >> q;
  for (int t=0; t<q; ++t) {
    int x,y;
    cin >> x >> y; --x; --y;
    cout << (G[x][y] ? W[x][y] : -1) << endl;
  }
  return 0;
}
