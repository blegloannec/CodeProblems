/*
  a tree is a bipartite graph, max path can be made 1
  by orienting all edges from one component to the other
*/
#include <iostream>
#include <vector>
using namespace std;

int N;
vector< vector<int> > T;
vector<bool> Color;

void dfs2color(int u=0, int u0=-1) {
  for (int v : T[u])
    if (v!=u0) {
      Color[v] = !Color[u];
      dfs2color(v, u);
    }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> N;
  T.resize(N);
  vector< pair<int,int> > E;
  for (int i=0; i<N-1; ++i) {
    int u,v;
    cin >> u >> v; --u; --v;
    T[u].push_back(v);
    T[v].push_back(u);
    E.push_back(make_pair(u,v));
  }
  Color.resize(N, true);
  dfs2color();
  for (const auto &e : E)
    cout << (int)Color[e.first] << '\n';
  return 0;
}
