#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<int> X,Y;

struct edge {
  int u, v, d;
  
  edge(int u, int v) : u(u), v(v) {
    d = abs(X[u]-X[v]) + abs(Y[u]-Y[v]);
  }
  
  bool operator<(const edge &e) const {
    return d > e.d;
  }
};

vector<edge> Edges;
vector<int> Tarj;
vector<bool> TarjInvColor;
// TarjInvColor[u] is true <=> u and Tarj[u] have distinct colors

void tarj_find(int u, int &u0, bool &col) {
  if (Tarj[u]<0) {
    u0 = u;
    col = false;
  }
  else {
    int ru0; bool cu0;
    tarj_find(Tarj[u], ru0, cu0);
    u0 = ru0;
    col = cu0 ^ TarjInvColor[u];
    Tarj[u] = u0;
    TarjInvColor[u] = col;
  }
}

bool tarj_union(int u, int v) {
  int ru,rv; bool cu,cv;
  tarj_find(u,ru,cu);
  tarj_find(v,rv,cv);
  if (ru!=rv) {
    /*
      we merge both components.
      we need furthermore to flip the colors of the rv component iff
      the colors of the newly linked vertices are currently the same.
    */
    Tarj[rv] = ru;
    TarjInvColor[rv] = cu==cv;
  }
  else if (cu==cv) return false; // FAIL: already same subgraph & same color!
  return true;
}

int main() {
  cin >> N;
  X.resize(N); Y.resize(N);
  for (int i=0; i<N; ++i) cin >> X[i] >> Y[i];
  for (int u=0; u<N; ++u)
    for (int v=u+1; v<N; ++v)
      Edges.push_back(edge(u,v));
  sort(Edges.begin(), Edges.end());
  Tarj.resize(N,-1); TarjInvColor.resize(N,false);
  int res = 0;
  for (const edge &e : Edges) {
    /*
      We want to break the current edge by separating u and v.
      This is equivalent to add this edge to a bipartite graph while
      maintaining it bipartite.
      We use classical union-find + 1 color bit. Each component
      represent one bipartite subgraph.
    */
    if (!tarj_union(e.u,e.v)) {
      res = e.d;
      break;
    }
  }
  cout << res << endl;
  return 0;
}
