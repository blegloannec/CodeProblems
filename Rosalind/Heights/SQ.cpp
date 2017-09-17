#include <iostream>
#include <vector>
using namespace std;

int n;
vector< vector<bool> > G;

/*
  O(n^3) checking for each u,v if the intersection of Neigh(u) with Neigh(v)
  contains 2 elements other than u and v (scanning through both lines of the
  adjacency matrix).
  This could also be done using adjacency sets ("unordered", i.e. hash tables)
  intersections, less straightforward, more efficient for sparse graphs, yet
  still O(n^3) in the worst case.
  This could also be simplified/done by computing G^2 or G^4 (for G the
  adjacency matrix), yet still requires O(n^3) with standard matrix
  multiplications.
*/

bool square() {
  for (int u=0; u<n; ++u)
    for (int v=u+1; v<n; ++v) {
      int cpt = 0;
      for (int w=0; w<n; ++w) {
	if (w==u || w==v) continue;
	if (G[u][w] && G[v][w]) {
	  ++cpt;
	  if (cpt==2) return true;
	}
      }
    }
  return false;
}

int main() {
  int k;
  cin >> k;
  for (int t=1; t<=k; ++t) {
    int m;
    cin >> n >> m;
    G.resize(n);
    for (int i=0; i<n; ++i) {
      G[i].resize(n);
      fill(G[i].begin(),G[i].end(),false);
    }
    for (int i=0; i<m; ++i) {
      int u,v;
      cin >> u >> v; --u; --v;
      G[u][v] = G[v][u] = true;
    }
    cout << (square() ? 1 : -1) << (t==k ? '\n' : ' ');
  }
  return 0;
}
