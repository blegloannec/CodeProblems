#include <iostream>
#include <vector>
using namespace std;

typedef vector< vector<int> > graph;
typedef vector< pair<int,int> > formula;

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

// numero du litteral -n <= a <= n, u =/= 0
int vert(int a) {
  return 2*(abs(a)-1)+(a<0?1:0);
}

// litteral a l'indice 0 <= u < 2n
int litt(int u) {
  return u&1 ? -(u/2+1) : u/2+1;
}

bool two_sat(int n, formula &F, vector<bool> &distrib) {
  // construction du graphe associe a la formule
  graph G(2*n);
  for (auto it=F.begin(); it!=F.end(); ++it) {
    int a = it->first, b = it->second; //  a V b
    G[vert(-a)].push_back(vert(b));    // ~a => b
    G[vert(-b)].push_back(vert(a));    // ~b => a
  }
  // calcul des composantes fortement connexes
  vector<int> comp_num;
  int nc = strongly_connected_components(G,comp_num);
  // satisfiable ssi les litteraux opposes sont dans des composantes dictinctes
  for (int a=1; a<=n; ++a)
    if (comp_num[vert(a)]==comp_num[vert(-a)]) return false;
  // on liste le contenu des composantes
  vector< vector<int> > comp(nc);
  for (int u=0; u<2*n; ++u) comp[comp_num[u]].push_back(litt(u));
  vector<bool> comp_seen(nc,false);
  distrib.resize(n);
  // on affecte les composantes dans l'ordre topologique inverse
  for (int c=nc-1; c>=0; --c)
    if (!comp_seen[c]) {
      comp_seen[c] = true;
      // on marque aussi la composante complementaire symetrique
      // (csym est parfaitement symetrique de c et contient les opposes
      //  des litteraux de c)
      int csym = comp_num[vert(-comp[c][0])]; 
      comp_seen[csym] = true;
      // on affecte vrai a tous les litteraux de c
      for (auto ia=comp[c].begin(); ia!=comp[c].end(); ++ia)
	distrib[abs(*ia)-1] = (*ia>0);
    }
  return true;
}

int main() {
  int k;
  cin >> k;
  for (int t=1; t<=k; ++t) {
    int n,m;
    cin >> n >> m;
    formula F;
    for (int i=0; i<m; ++i) {
      int a,b;
      cin >> a >> b;
      F.push_back(make_pair(a,b));
    }
    vector<bool> distrib;
    if (two_sat(n,F,distrib)) {
      cout << "1 ";
      for (int i=0; i<n; ++i)
	cout << (distrib[i] ? i+1 : -(i+1)) << (i==n-1?'\n':' ');
    }
    else cout << 0 << endl;
  }
  return 0;
}
