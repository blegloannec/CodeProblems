#include <iostream>
#include <cstdio>
#include "graph.h"
#include "dijkstra.h"

double rand_proba() {
  return (double)rand() / (double)RAND_MAX;
}

weight rand_weight() {
  return rand()>>16;
}

graph generate_random_edges(int n, int m, bool directed=true) {
  graph G(n);
  for (int e=0; e<m; ++e) {
    int u = rand()%n, v = rand()%n;
    weight w = rand_weight();
    G[u].push_back(edge(v, w));
    if (!directed)
      G[v].push_back(edge(u, w));
  }
  return G;
}

graph generate_edge_proba(int n, double p, bool directed=true) {
  graph G(n);
  for (int u=0; u<n; ++u) {
    int v0 = directed ? 0 : u+1;
    for (int v=v0; v<n; ++v)
      if ((double)rand()/(double)RAND_MAX < p) {
	weight w = rand_weight(); 
	G[u].push_back(edge(v, w));
	if (!directed)
	  G[v].push_back(edge(u, w));
      }
  }
  return G;
}

int main() {
  srand(42);
  graph G = generate_random_edges(10000, 20000);
  vector<weight> Dist = dijkstra(G, 0);
  return 0;
}
