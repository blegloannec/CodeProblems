/*
  Euclidean MST problem
  https://en.wikipedia.org/wiki/Euclidean_minimum_spanning_tree
  Building the graph in O(n²) and use general MST algorithms is good
  enough here (done in the following).
  This can however be solved faster as an EMST can always be obtained
  as a MST of a Delauney triangulation (of size O(n)).
*/
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

typedef pair< double, pair<int,int> > edge;
#define _d2_ first
#define _i_ second.first
#define _j_ second.second
#define make_edge(d,i,j) make_pair((d), make_pair((i),(j)))

#define SQR(x) ((x)*(x))

int N;
vector<edge> E;
vector<int> T;

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

bool merge(int x, int y) {
  int x0 = find(x), y0 = find(y);
  if (x0==y0) return false;
  T[y0] = x0;
  return true;
}

double MST() {
  sort(E.begin(), E.end());
  T.resize(N, -1);
  double s = 0.;
  int C = N;
  for (int e=0; C>1; ++e)
    if (merge((E[e]._i_), (E[e]._j_))) {
      s += sqrt(E[e]._d2_);
      --C;
    }
  return s;
}

int main() {
  int C;
  scanf("%d", &C);
  for (int c=0; c<C; ++c) {
    scanf("%d", &N);
    vector<double> X(N), Y(N);
    for (int i=0; i<N; ++i)
      scanf("%lf %lf", &X[i], &Y[i]);
    for (int i=0; i<N; ++i)
      for (int j=i+1; j<N; ++j) {
	double d2 = SQR(X[i]-X[j]) + SQR(Y[i]-Y[j]);
	E.push_back(make_edge(d2,i,j));
      }
    printf("%.2lf\n", MST());
    // cleaning
    E.clear();
    T.clear();
  }
  return 0;
}
