#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include "graph.h"
#include "dijkstra.h"
#include "bellman_ford.h"
#include "desopo_pape.h"
#include "dijkstra_custom_heap.h"

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
      if (rand_proba() < p) {
	weight w = rand_weight(); 
	G[u].push_back(edge(v, w));
	if (!directed)
	  G[v].push_back(edge(u, w));
      }
  }
  return G;
}

int main() {
  srand(time(NULL));
  //int n = 50000;
  //graph G = generate_random_edges(n, 2000*n);
  graph G = generate_edge_proba(10000, 0.3);
  
  clock_t t0, t1;
  double dt;
  
  /*
  t0 = clock();
  vector<weight> Dist0 = bellman_ford(G, 0);
  t1 = clock();
  dt = (double)(t1-t0) / (double)CLOCKS_PER_SEC;
  cout << "BF " << dt << endl; 
  */
  
  t0 = clock();
  vector<weight> Dist1 = dijkstra(G, 0);
  t1 = clock();
  dt = (double)(t1-t0) / (double)CLOCKS_PER_SEC;
  cout << "Dij   " << dt << endl;
  
  t0 = clock();
  vector<weight> Dist2 = dijkstra_custom_heap(G, 0);
  t1 = clock();
  dt = (double)(t1-t0) / (double)CLOCKS_PER_SEC;
  cout << "Dij2  " << dt << endl;
  
  t0 = clock();
  vector<weight> Dist3 = desopo_pape(G, 0);
  t1 = clock();
  dt = (double)(t1-t0) / (double)CLOCKS_PER_SEC;
  cout << "DP    " << dt << endl;
  
  //assert(Dist1==Dist0);
  assert(Dist1==Dist2);
  assert(Dist1==Dist3);
  return 0;
}
