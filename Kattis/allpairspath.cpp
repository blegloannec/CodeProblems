#include <iostream>
#include <vector>
using namespace std;

int n;
vector< vector<bool> > G,MInf;
vector< vector<int> > W;

void init() {
  G.clear();
  W.clear();
  MInf.clear();
  G.resize(n);
  W.resize(n);
  MInf.resize(n);
  for (int i=0; i<n; ++i) {
    G[i].resize(n,false);
    W[i].resize(n);
    MInf[i].resize(n,false);
    G[i][i] = true;
    W[i][i] = 0;
  }
}

void floyd_warshall() {
  for (int k=0; k<n; ++k)
    for (int u=0; u<n; ++u)
      for (int v=0; v<n; ++v)
	if (G[u][k] && G[k][v]) {
	  if (G[u][v]) W[u][v] = min(W[u][v],W[u][k]+W[k][v]);
	  else {
	    G[u][v] = true;
	    W[u][v] = W[u][k]+W[k][v];
	  }
	}
  // flagging -inf path in O(n^3)
  for (int u=0; u<n; ++u)
    if (W[u][u]<0)        // negative loop on u
      for (int v=0; v<n; ++v)
	if (G[v][u])      // v ~~> u
	  for (int w=0; w<n; ++w)
	    if (G[u][w])  // u ~~> w
	      MInf[v][w] = true;
}

int main() {
  int m,q;
  bool first = true;
  while (cin >> n >> m >> q) {
    if (n==0) break;
    if (first) first = false;
    else cout << endl;
    init();
    for (int i=0; i<m; ++i) {
      int u,v,w;
      cin >> u >> v >> w;
      if (G[u][v]) W[u][v] = min(W[u][v],w);
      else {
	G[u][v] = true;
	W[u][v] = w;
      }
    }
    floyd_warshall();
    for (int i=0; i<q; ++i) {
      int u,v;
      cin >> u >> v;
      if (MInf[u][v]) cout << "-Infinity" << endl;
      else if (G[u][v]) cout << W[u][v] << endl;
      else cout << "Impossible" << endl;
    }
  }
  return 0;
}
