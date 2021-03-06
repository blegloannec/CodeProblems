#include "graph.h"
#include <queue>

vector<weight> dijkstra(const graph &G, int u0) {
  int n = G.size();
  vector<weight> Dist(n, INF);
  Dist[u0] = 0;
  priority_queue< pair<weight,int> > Q;
  Q.push(make_pair(-Dist[u0], u0));
  while (!Q.empty()) {
    weight d = -Q.top().first;
    int u = Q.top().second;
    Q.pop();
    if (Dist[u]<d) continue;
    for (const edge &e : G[u]) {
      int v = e._v_;
      weight w = e._w_;
      if (Dist[u]+w < Dist[v]) {
	Dist[v] = Dist[u]+w;
	Q.push(make_pair(-Dist[v], v));
      }
    }
  }
  return Dist;
}
