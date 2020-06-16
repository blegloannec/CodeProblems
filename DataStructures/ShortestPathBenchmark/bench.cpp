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

vector<double> test_graph(const graph &G, bool run_quad=true) {
  vector<double> T;
  {
    double dt = -1;
    if (run_quad) {
      clock_t t0 = clock();
      vector<weight> Dist0 = bellman_ford(G, 0);
      clock_t t1 = clock();
      dt = (double)(t1-t0) / (double)CLOCKS_PER_SEC;
    }
    T.push_back(dt);
  }
  {
    clock_t t0 = clock();
    vector<weight> Dist1 = dijkstra(G, 0);
    clock_t t1 = clock();
    double dt = (double)(t1-t0) / (double)CLOCKS_PER_SEC;
    T.push_back(dt);
  }
  {
    clock_t t0 = clock();
    vector<weight> Dist2 = dijkstra_custom_heap(G, 0);
    clock_t t1 = clock();
    double dt = (double)(t1-t0) / (double)CLOCKS_PER_SEC;
    T.push_back(dt);
  }
  {
    clock_t t0 = clock();
    vector<weight> Dist3 = desopo_pape(G, 0);
    clock_t t1 = clock();
    double dt = (double)(t1-t0) / (double)CLOCKS_PER_SEC;
    T.push_back(dt);
  }
  return T;
}

/*
vector<double> avg_edge_mode(int n, int m, int nb=50) {
  vector<double> S;
  for (int i=0; i<nb; ++i) {
    vector<double> 
  }
  for (int i=0; i<4
}
*/

int main(int argc, char *argv[]) {
  srand(time(NULL));
  //int n = 50000;
  //graph G = generate_random_edges(n, 2000*n);
  graph G = generate_edge_proba(10000, 0.3);
  test_graph(G, false);
  return 0;
}
