#include "graph.h"

vector<weight> bellman_ford(const graph &G, int u0) {
  int n = G.size();
  vector<weight> Dist(n, INF);
  Dist[u0] = 0;
  for (int k=0; k<n-1; ++k)
    for (int u=0; u<n; ++u)
      if (Dist[u]<INF)
	for (const edge &e : G[u]) {
	  int v = e._v_;
	  weight w = e._w_;
	  Dist[v] = min(Dist[v], Dist[u] + w);
	}
  return Dist;
}
