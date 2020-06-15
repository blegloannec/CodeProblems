#include "graph.h"
#include <deque>

vector<weight> desopo_pape(const graph &G, int u0) {
  int n = G.size();
  vector<weight> Dist(n, INF);
  Dist[u0] = 0;
  deque<int> Q;
  vector<bool> inQ(n, false);
  Q.push_back(u0);
  inQ[u0] = true;
  while (!Q.empty()) {
    int u = Q.front();
    Q.pop_front();
    inQ[u] = false;
    for (const edge &e : G[u]) {
      int v = e._v_;
      weight w = e._w_;
      if (Dist[v]==INF) {
	Dist[v] = Dist[u]+w;
	Q.push_back(v);
	inQ[v] = true;
      }
      else if (Dist[u]+w < Dist[v]) {
	Dist[v] = Dist[u]+w;
	if (!inQ[v]) {
	  Q.push_front(v);
	  inQ[v] = true;
	}
      }
    }
  }
  return Dist;
}
