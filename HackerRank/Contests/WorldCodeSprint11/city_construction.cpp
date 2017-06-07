#include <cstdio>
#include <vector>
#include <bitset>
using namespace std;

/*
  Les sommets ajoutes par les requetes sont seuls dans leur composante
  fortement connexe.
  On constuit le graphe final, on calcule les composantes fortement connexes,
  on constuit leur DAG, puis, pour finir, on construit sa cloture transitive.
  Enfin on repond aux requetes de type 2.
*/

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

int main() {
  int n,m,u,v,q,c,x,y;
  scanf("%d %d",&n,&m);
  graph G(n);
  for (int i=0; i<m; ++i) {
    scanf("%d %d",&u,&v); --u; --v;
    G[u].push_back(v);
  }
  scanf("%d",&q);
  vector<int> X,Y;
  for (int i=0; i<q; ++i) {
    scanf("%d %d %d",&c,&x,&y);
    if (c==1) {
      G.resize(++n);
      if (y==0) G[x-1].push_back(n-1);
      else G[n-1].push_back(x-1);
    }
    else {
      X.push_back(x-1);
      Y.push_back(y-1);
    }
  }
  vector<int> compo;
  int nbc = strongly_connected_components(G,compo);
  // on utilise des bitsets et non des listes de successeurs pour economiser
  // la memoire (de plus c'est un peu plus rapide ici)
  vector< bitset<50001> > C(nbc);
  // construction du graphe des composantes fortement connexes
  for (int u=0; u<n; ++u)
    for (vector<int>::iterator it=G[u].begin(); it!=G[u].end(); ++it)
      C[compo[u]][compo[*it]] = 1;
  // cloture transitive
  vector< bitset<50001> > CC(nbc);
  for (int c=nbc-1; c>=0; --c) {
    CC[c][c] = 1;
    for (int d=0; d<nbc; ++d)
      if (C[c][d]) CC[c] |= CC[d];
  }
  for (unsigned int i=0; i<X.size(); ++i) {
    int cx = compo[X[i]], cy = compo[Y[i]];
    if (CC[cx][cy]) printf("Yes\n");
    else printf("No\n");
  }
  return 0;
}
