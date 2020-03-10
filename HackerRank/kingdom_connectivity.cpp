#include <iostream>
#include <vector>
using namespace std;
using ll = long long;


/* ===== Strongly Connected Components ===== */
typedef vector< vector<int> > graph;

void reverse_graph(graph &G, graph &R) {
  R.resize(G.size());
  for (unsigned int u=0; u<G.size(); ++u)
    for (vector<int>::iterator it=G[u].begin(); it!=G[u].end(); ++it)
      R[*it].push_back(u);
}

void dfs_topo(graph &G, int u, vector<bool> &seen, vector<int> &topo) {
  if (seen[u]) return;
  seen[u] = true;
  for (vector<int>::iterator it=G[u].begin(); it!=G[u].end(); ++it)
    dfs_topo(G,*it,seen,topo);
  topo.push_back(u);
}

void dfs_compo(graph &G, int u, int c, vector<int> &compo) {
  if (compo[u]>=0) return;
  compo[u] = c;
  for (vector<int>::iterator it=G[u].begin(); it!=G[u].end(); ++it)
    dfs_compo(G,*it,c,compo);
}

int strongly_connected_components(graph &G, vector<int> &compo) {
  int N = G.size();
  vector<bool> seen(N,false);
  vector<int> topo;
  for (int u=0; u<N; ++u) dfs_topo(G,u,seen,topo);
  graph R;
  reverse_graph(G,R);
  compo.resize(N,-1);
  int c = 0;
  for (int i=N-1; i>=0; --i)
    if (compo[topo[i]]<0) {
      dfs_compo(R,topo[i],c,compo);
      ++c;
    }
  return c;
}
/* ===== End SCC ===== */


void dfs_reach(const graph &G, int u, vector<bool> &seen) {
  seen[u] = true;
  for (int v : G[u])
    if (!seen[v]) dfs_reach(G,v,seen);
}

const ll MOD = 1000000000;
ll dag_path_dp(const graph &DAGinv, const vector<bool> &reachable, int u, vector<ll> &memo) {
  if (memo[u]<0) {
    ll res = 0;
    for (int u0 : DAGinv[u])
      if (reachable[u0])
	res = (res + dag_path_dp(DAGinv,reachable,u0,memo)) % MOD;
    memo[u] = res;
  }
  return memo[u];
}

int main() {
  // Input
  int n,m;
  cin >> n >> m;
  graph G(n);
  for (int i=0; i<m; ++i) {
    int u,v;
    cin >> u >> v;
    G[u-1].push_back(v-1);
  }
  // Components
  vector<int> compo;
  int compo_cnt = strongly_connected_components(G,compo);
  // Components sizes
  vector<int> compo_size(compo_cnt,0);
  for (int u=0; u<n; ++u) ++compo_size[compo[u]];
  // Components DAG and inverse
  graph DAG(compo_cnt), DAGinv(compo_cnt);
  for (int u=0; u<n; ++u)
    for (int v : G[u])
      if (compo[u]!=compo[v]) {
	DAG[compo[u]].push_back(compo[v]);
	DAGinv[compo[v]].push_back(compo[u]);
      }
  // Marking reachable components from both ends
  // and detecting reachable loop (reachable component with >1 vertex)
  vector<bool> reachable(compo_cnt,false), reachable_inv(compo_cnt,false);
  dfs_reach(DAG, compo[0], reachable);
  dfs_reach(DAGinv, compo[n-1], reachable_inv);
  bool loop = false;
  for (int c=0; c<compo_cnt; ++c) {
    reachable[c] = reachable[c] && reachable_inv[c];
    if (reachable[c] && compo_size[c]>1) {
      loop = true;
      break;
    }
  }
  if (loop) cout << "INFINITE PATHS\n";
  else {
    // Counting paths through DP on the DAG
    vector<ll> memo(compo_cnt,-1);
    memo[compo[0]] = 1;
    cout << dag_path_dp(DAGinv,reachable,compo[n-1],memo) << endl;
  }
  return 0;
}
