/*
  Euclidean MST problem
  https://en.wikipedia.org/wiki/Euclidean_minimum_spanning_tree
  Use general MST algorithms in O(n²) is good enough here.
  Prim is much faster than Kruskal in this case as it allows to only
  compute the useful edges (linking a not yet selected vertex) on-the-fly
  instead of computing & sorting everything at the beginning.
  This can however be solved faster as an EMST can always be obtained
  as a MST of a Delauney triangulation (of size O(n)).
*/
#include <cstdio>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

#define SQR(x) ((x)*(x))

int N;
vector<double> X(N), Y(N);

double dist(int i, int j) {
  return sqrt(SQR(X[i]-X[j]) + SQR(Y[i]-Y[j]));
}

double prim(int u0=0) {
  double mst = 0.;
  vector<double> Dist(N, 1e30);
  Dist[u0] = 0.;
  vector<double> Seen(N, false);
  priority_queue< pair<double,int> > Q;
  Q.push(make_pair(0.,u0));
  while (!Q.empty()) {
    int u = Q.top().second;
    Q.pop();
    if (Seen[u]) continue;
    Seen[u] = true;
    mst += Dist[u];
    for (int v=0; v<N; ++v)
      if (!Seen[v]) {
	double d = dist(u,v);
	if (d<Dist[v]) {
	  Dist[v] = d;
	  Q.push(make_pair(-d,v));
	}
      }
  }
  return mst;
}

int main() {
  int C;
  scanf("%d", &C);
  for (int c=0; c<C; ++c) {
    scanf("%d", &N);
    X.resize(N); Y.resize(N);
    for (int i=0; i<N; ++i)
      scanf("%lf %lf", &X[i], &Y[i]);
    printf("%.2lf\n", prim());
  }
  return 0;
}
