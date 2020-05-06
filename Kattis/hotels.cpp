#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int F, E;
vector<int> R, M, Dist;
vector< vector<int> > G;

int dist2elev(int f, int i) {
  if (f<=R[i]) return R[i]-f;
  int e = ((f-R[i])/M[i])*M[i] + R[i];
  int d = f-e;
  e += M[i];
  if (e<F) d = min(d, e-f);
  return d;
}

void dijkstra() {
  Dist = R;
  priority_queue< pair<int,int> > Q;
  for (int u=0; u<E; ++u) Q.push(make_pair(-Dist[u], u));
  while (!Q.empty()) {
    auto du = Q.top();
    Q.pop();
    int d = -du.first, u = du.second;
    if (d>Dist[u]) continue;
    for (int v=0; v<E; ++v)
      if (v!=u && d+G[u][v]<Dist[v]) {
	Dist[v] = d + G[u][v];
	Q.push(make_pair(-Dist[v], v));
      }
  }
}

void elev_graph() {
  G.clear();
  G.resize(E, vector<int>(E, 0));
  for (int i=0; i<E; ++i)
    for (int j=i+1; j<E; ++j) {
      int d = F;
      for (int x = R[i]; x<F && d>0; x += M[i])
	d = min(d, dist2elev(x, j));
      G[i][j] = G[j][i] = d;
    }
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> F >> E;
    R.resize(E);
    M.resize(E);
    for (int i=0; i<E; ++i)
      cin >> R[i] >> M[i];
    if (E==0) {  // no elevators
      cout << F-1 << ' ' << F-1 << endl;
      continue;
    }
    // building elevators graph & elevator-to-elevator distances
    elev_graph();
    // computing distances from 0 to each elevator
    dijkstra();
    // sorting in O(N log E)
    vector< pair<int,int> > X;
    priority_queue< pair<int,int> > H;
    for (int i=0; i<E; ++i) H.push(make_pair(-R[i], i));
    while (!H.empty()) {
      auto xi = H.top();
      H.pop();
      int x = -xi.first, i = xi.second;
      X.push_back(make_pair(x, i));
      x += M[i];
      if (x<F) H.push(make_pair(-x, i));
    }
    // computing worst floor
    int dmax = 0, fmax = 0;
    { // worst position within 0 -> first elevator
      int x1 = X[0].first, d1 = Dist[X[0].second];
      int x = (d1+x1)/2;
      if (x>dmax) dmax = fmax = x;
    }
    for (int i=0; i+1<(int)X.size(); ++i) {
      int x1 = X[i].first,   d1 = Dist[X[i].second];
      int x2 = X[i+1].first, d2 = Dist[X[i+1].second];
      /*
	worst intermediate position x verifies
	d1 + x-x1 = d2 + x2-x
      */
      int x = min(max(x1, (d2-d1+x1+x2)/2), x2);
      int d = d1 + x-x1;
      if (d>dmax) { dmax = d; fmax = x; }
    }
    { // last floor
      int x1 = X.back().first, d1 = Dist[X.back().second];
      int x = F-1;
      int d = d1 + x-x1;
      if (d>dmax) { dmax = d; fmax = x; }
    }
    cout << dmax << ' ' << fmax << endl;
  }
  return 0;
}
