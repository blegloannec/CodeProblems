#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

struct edge {
  int v, c, p;
  edge(int v, int c, int p) : v(v), c(c), p(p) {}
};

int B, N;
vector< vector<edge> > Pred;
vector<int> Cost, Pres;

void compute_cost(int u) {
  if (Cost[u]<0) {
    if (Pred[u].empty())
      Cost[u] = Pres[u] = 0;
    else {
      Cost[u] = 1<<20;
      for (const edge &e : Pred[u]) {
	compute_cost(e.v);
	if (Cost[e.v]+e.c<Cost[u]) {
	  Cost[u] = Cost[e.v]+e.c;
	  Pres[u] = Pres[e.v]+e.p;
	}
	else if (Cost[e.v]+e.c==Cost[u] && Pres[e.v]+e.p>Pres[u])
	  Pres[u] = Pres[e.v]+e.p;
      }
    }
  }
}

void knapsack(int &pmax, int &cmin) {
  vector<int> P(B+1, 0);
  for (int i=0; i<N; ++i)
    for (int c=B-Cost[i]; c>=0; --c)
      P[c+Cost[i]] = max(P[c+Cost[i]], P[c]+Pres[i]);
  pmax = cmin = 0;
  for (int c=0; c<=B; ++c)
    if (P[c]>pmax) {
      pmax = P[c];
      cmin = c;
    }
}

int main() {
  cin >> B;
  int M;
  cin >> M;
  unordered_map<string,int> NameIdx;
  N = 0;
  for (int i=0; i<M; ++i) {
    string new_recipe, base_recipe, ingr;
    int cost, pres;
    cin >> new_recipe >> base_recipe >> ingr >> cost >> pres;
    if (NameIdx.find(base_recipe)==NameIdx.end()) {
      NameIdx[base_recipe] = N++;
      Pred.resize(N);
    }
    if (NameIdx.find(new_recipe)==NameIdx.end()) {
      NameIdx[new_recipe] = N++;
      Pred.resize(N);
    }
    int v = NameIdx[new_recipe], u = NameIdx[base_recipe];
    Pred[v].push_back(edge(u, cost, pres));
  }
  Cost.resize(N, -1);
  Pres.resize(N, -1);
  for (int i=0; i<N; ++i) compute_cost(i);
  int pmax, cmin;
  knapsack(pmax, cmin);
  cout << pmax << endl;
  cout << cmin << endl;
  return 0;
}
