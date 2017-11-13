#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

/*
  Considerons l'arbre a un instant donne.
  L'observation essentielle est la suivante : si x et y sont 2 sommets qui ne
  sont pas des banques et tels que le (plus court) chemin de x a y ne comporte
  pas de banque, alors les sommets "accessibles" (i.e. en passant par une
  banque) depuis x sont les memes que depuis y. En effet, on a pour tout z :
    x ---- w ---- y   avec w sur le chemin x--y, possiblement confondu avec
           |          x ou y, mais le chemin x--w--y ne comporte pas de banque
           |          donc si banque il y a c'est sur w--z et cela revient
           z          donc au meme pour x et y.
  Des lors, si l'on deconnecte les banques de l'arbre (en retirant les aretes
  adjacentes aux banques), alors les composantes connexes forment :
   - les ensembles de sommets non banques connectes sans passer par une banque,
     pour lesquels la reponse est la meme et est exactement le deuxieme plus
     grand sommet du complementaire de la composante ;
   - les banques, seules dans leur composante, pour lesquels la reponse est
     simplement le sommet n-1 (deuxieme plus grand sommet de l'arbre).
  Algo offline : on traite les requetes en ordre inverse en reconnectant l'arbre
  (union-find) progressivement au fur et a mesure que les banques disparaissent
  et en resolvant chaque requete en O(log n) en utilisant un (bi-)max segment
  tree stockant les 2 plus grands sommets de chaque composante.
*/

int N,M;
vector< pair<int,int> > Q;
vector< vector<int> > G;
vector<int> B;

struct bimax {
  int m0,m1;
  bimax(int m0=-1, int m1=-1) : m0(m0), m1(m1) {}
};

bimax bimerge(const bimax &A, const bimax &B) {
  int m0 = A.m0, m1 = A.m1;
  if (B.m0>m0) {
    m1 = m0;
    m0 = B.m0;
  }
  else if (B.m0>m1) m1 = B.m0;
  if (B.m1>m1) m1 = B.m1;
  return bimax(m0,m1);
}

typedef bimax elem;

struct SegmentTree {
  const elem NEUTRAL = bimax(); // neutre pour l'operation
  unsigned int N;
  vector<elem> S;

  // operation utilisee
  static elem op(elem a, elem b) {
    return bimerge(a,b);
  }
  
  SegmentTree(const vector<elem> &T) {
    N = 1;
    while (N<T.size()) N <<= 1;
    S.resize(2*N,NEUTRAL);
    for (unsigned int i=0; i<T.size(); ++i) S[N+i] = T[i];
    for (int p=N-1; p>0; --p) S[p] = op(S[2*p],S[2*p+1]);
  }

  elem get(int i) const {
    return S[N+i];
  }

  void set(int i, elem v) {
    unsigned int p = N+i;
    S[p] = v;
    p >>= 1;
    while (p>0) {
      S[p] = op(S[2*p],S[2*p+1]);
      p >>= 1;
    }
  }

  elem _range(int p, int start, int span, int i, int j) const {
    // returns the minimum in t in the indexes [i,j) intersected
    // with [start,start+span)
    if (start+span<=i || j<=start) return NEUTRAL;
    if (i<=start && start+span<=j) return S[p];
    elem left = _range(2*p,start,span/2,i,j);
    elem right = _range(2*p+1,start+span/2,span/2,i,j);
    return op(left,right);
  }
  
  // returns op{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) const {
    return _range(1,0,N,i,j+1);
  }
};

vector<int> Tarj;

int find(int x) {
  if (Tarj[x]<0) return x;
  Tarj[x] = find(Tarj[x]);
  return Tarj[x];
}

void merge(int x, int y, SegmentTree &ST) {
  int x0 = find(x), y0 = find(y);
  Tarj[y0] = x0;
  ST.set(x0,bimerge(ST.get(x0),ST.get(y0)));
  ST.set(y0,bimax());
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    int M;
    scanf("%d %d",&N,&M);
    G.resize(N);
    for (int i=0; i<N-1; ++i) {
      int u,v;
      scanf("%d %d",&u,&v); --u; --v,
      G[u].push_back(v);
      G[v].push_back(u);
    }
    B.resize(N,0);    
    for (int q=0; q<M; ++q) {
      int c,C;
      scanf("%d %d",&c,&C); --C;
      if (c==1) ++B[C];
      Q.push_back(make_pair(c,C));
    }
    Tarj.resize(N,-1);
    vector<bimax> T0(N);
    for (int u=0; u<N; ++u) T0[u] = bimax(u);
    SegmentTree ST(T0);
    for (int u=0; u<N; ++u)
      if (!B[u])
	for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
	  if (B[*iv]==0 && find(u)!=find(*iv))
	    merge(u,*iv,ST);
    vector<int> res(M);
    for (int q=M-1; q>=0; --q) {
      if (Q[q].first==1) {
	int u = Q[q].second;
	--B[u];
	if (B[u]==0)
	  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
	    if (B[*iv]==0) merge(u,*iv,ST);
      }
      else {
	int u = Q[q].second;
	if (B[u]>0) res[q] = N-2;
	else {
	  u = find(u);
	  res[q] = bimerge((u>0?ST.range(0,u-1):bimax()),(u<N-1?ST.range(u+1,N-1):bimax())).m1;
	}
      }
    }
    for (int q=0; q<M; ++q)
      if (Q[q].first==2) printf("%d\n",res[q]>=0?res[q]+1:-1);
    // cleaning
    G.clear();
    B.clear();
    Q.clear();
    Tarj.clear();
  }
  return 0;
}
