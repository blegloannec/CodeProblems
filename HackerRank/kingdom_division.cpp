#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

const ll P = 1000000007;
int N;
vector< vector<int> > T;
vector<ll> Count, CountIsolatedRoot;

void mul(ll &a, ll b) {
  a = (a*b) % P;
}

/*
  O(N) DP on the tree
  We arbitrarily root the tree and compute for each vertex u, assuming the
  color of u is fixed (i.e. we consider half the colorings):
    Count[u] = the number of valid colorings of the subtree rooted at u
    CountIsolatedRoot[u] = the number of almost valid colorings of the subtree
                           rooted at u where only u is isolated
*/
void dp_dfs(int u=0, int u0=-1) {
  if (u0>=0 && T[u].size()==1) Count[u] = 0;
  else {
    bool leaf_child = false;
    for (int v : T[u])
      if (v!=u0) {
	dp_dfs(v,u);
	mul(CountIsolatedRoot[u], Count[v]);
	mul(Count[u], ((2*Count[v])%P + CountIsolatedRoot[v])%P);
	leaf_child = leaf_child || T[v].size()==1;
      }
    if (leaf_child) CountIsolatedRoot[u] = 0;
    else {
      Count[u] -= CountIsolatedRoot[u];
      if (Count[u]<0) Count[u] += P;
    }
  }
}

int main() {
  cin >> N;
  T.resize(N);
  for (int i=0; i<N-1; ++i) {
    int u,v;
    cin >> u >> v; --u; --v;
    T[u].push_back(v);
    T[v].push_back(u);
  }
  Count.resize(N,1);
  CountIsolatedRoot.resize(N,1);
  dp_dfs();
  cout << (2*Count[0])%P << endl;
  return 0;
}
