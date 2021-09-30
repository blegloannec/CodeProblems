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

bool two_sat(int n, formula &F) { //, vector<bool> &distrib) {
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
  
  /*
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
  */
  
  return true;
}


/* 
  Actual problem code: reduction to 2-SAT
  We create a var. st(s) for the orient. of each street s
                   av(a)                         avenue a
  (we conveniently still denote them as s/a in the following)
  Each route gives the following constraint:
    (±s₁ ∧ ±a₂) ∨ (±s₂ ∧ ±a₁)
    where ±a depends on the sign of Δs
          ±s                        Δa
  We define variables sa(s,a,d) for (±s ∧ ±a)
  with d a 2-bit int indicating both ±
  We tie them to the s/a by adding constraints:
    sa(s,a,d) => ±s  (i.e. -sa(s,a,d) ∨ ±s)
    sa(s,a,d) => ±a
    where ± depends on the bits of d
  Each route now gives a proper constraint:
    sa(s₁,a₂,d) ∨ sa(s₂,a₁,d)
*/
int S,A;

int st(int s) {
  return s;
}

int av(int a) {
  return S + a;
}

int sa(int s, int a, int d) {
  return S+A + 1 + ((s-1)*A+(a-1))*4+d;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int M;
    cin >> S >> A >> M;
    formula F;
    for (int s=1; s<=S; ++s) {
      for (int a=1; a<=A; ++a) {
	F.push_back(make_pair(-sa(s,a,0),-st(s)));
	F.push_back(make_pair(-sa(s,a,0),-av(a)));
	F.push_back(make_pair(-sa(s,a,1), st(s)));
	F.push_back(make_pair(-sa(s,a,1),-av(a)));
	F.push_back(make_pair(-sa(s,a,2),-st(s)));
	F.push_back(make_pair(-sa(s,a,2), av(a)));
	F.push_back(make_pair(-sa(s,a,3), st(s)));
	F.push_back(make_pair(-sa(s,a,3), av(a)));
      }
    }
    for (int i=0; i<M; ++i) {
      int s1,a1,s2,a2;
      cin >> s1 >> a1 >> s2 >> a2;
      if (s1==s2 && a1==a2) continue;
      if (s1==s2) {
	int v = a1<a2 ? st(s1) : -st(s1);
	F.push_back(make_pair(v,v));
      }
      else if (a1==a2) {
	int v = s1<s2 ? av(a1) : -av(a1);
	F.push_back(make_pair(v,v));
      }
      else {
	int d = 0;
	if (s1<s2) d |= 2;
	if (a1<a2) d |= 1;
	F.push_back(make_pair(sa(s1,a2,d), sa(s2,a1,d)));
      }
    }
    int n = sa(S,A,3);
    cout << (two_sat(n, F) ? "Yes" : "No") << '\n';
  }
  return 0;
}
