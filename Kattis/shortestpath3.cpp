#include <iostream>
#include <vector>
using namespace std;

int n;
vector< vector< pair<int,int> > > G;
vector<int> Dist;
vector<bool> Reach,Neg;

void dfs_inf(int u) {
  Neg[u] = true;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (!Neg[iv->first]) dfs_inf(iv->first);
}

void bellman_ford(int u0=0) {
  Reach.resize(n,false);
  Reach[u0] = true;
  Dist.resize(n);
  Dist[u0] = 0;
  for (int k=0; k<n-1; ++k)
    for (int u=0; u<n; ++u)
      if (Reach[u])
	for (auto iv=G[u].begin(); iv<G[u].end(); ++iv) {
	  int v = iv->first, w = iv->second;
	  if (Reach[v])
	    Dist[v] = min(Dist[v], Dist[u] + w);
	  else {
	    Reach[v] = true;
	    Dist[v] = Dist[u] + w;
	  }
	}
  // checking for negative cycles and propagating the information
  Neg.resize(n,false);
  for (int u=0; u<n; ++u)
    if (Reach[u] && !Neg[u])
      for (auto iv=G[u].begin(); iv<G[u].end(); ++iv) {
	int v = iv->first, w = iv->second;
	if (!Neg[v] && Dist[u]+w<Dist[v]) dfs_inf(v);
      }
}

int main() {
  bool first = true;
  while (true) {
    int m,q,s;
    cin >> n >> m >> q >> s;
    if (n==0) break;
    if (first) first = false;
    else cout << endl;
    G.resize(n);
    for (int i=0; i<m; ++i) {
      int u,v,w;
      cin >> u >> v >> w;
      G[u].push_back(make_pair(v,w));
    }
    bellman_ford(s);
    for (int i=0; i<q; ++i) {
      int u;
      cin >> u;
      if (!Reach[u]) cout << "Impossible" << endl;
      else if (Neg[u]) cout << "-Infinity" << endl;
      else cout << Dist[u] << endl;
    }
    // cleaning
    G.clear();
    Dist.clear();
    Reach.clear();
    Neg.clear();
  }
  return 0;
}
