/*
  #(u,d,x) = le nb de valeurs A[v]<=x pour v a distance <=d de u dans l'arbre entier
  Si l'on sait calculer #() efficacement, alors on peut rechercher le k-ieme x par
  recherche dichotomique.
  Considerons une decomposition centroide pour avoir une hierarchie de
  profondeur O(log N). La zone (sous-arbre) de responsabilite d'un
  sommet u sera notee Zone(u) et son centroide parent dans la hierarchie P(u).
  Pour chaque sommet u, on construit une structure de donnees permettant de
  repondre efficacement à des requetes du type :
  Q(u,d,x) = le nb de valeurs A[v]<=x pour v a distance <=d de u dans *Zone(u)*
  Dans ce code, on utilisera une table 2D de sqrt(|Zone(u)|)^2 boites pour
  stocker les points {(dist(u,v), A[v]) pour v dans Zone(u)} et repondre
  aux requetes en O(sqrt(|Zone(u)|)).
  Pour repondre a une requete sur l'arbre entier, on introduit de plus :
  Q'(u,d,x) = le nb de valeurs A[v]<=x pour v a distance <=d de *P(u)* dans Zone(u)
              (et par convention 0 si u est le centroide racine, i.e. P(u) n'existe pas)
  (On calcule Q' de la meme facon que Q, mais en utilisant les distances a P(u) au lieu
   de u.)
  On a alors, pour v(0) = u, v(i+1) = P(v(i))  (suite finie de u au centroide racine)
  et en posant d(i) = max( 0, d - dist(u,v(i)) ) :
  #(u,d,x) = Sum_i  Q(v(i),d(i),x)  -  Q'(v(i-1),d(i),x) si i>0
                    elements de Zone(v(i)) a distance d(i) de v(i)
		    (et donc a distance d de u pour ceux n'appartenant
		    pas au sous-arbre contenant u)
                                    - ceux de Zone(v(i-1)) a distance d(i) de P(v(i-1)) = v(i)
				      (et donc appartenant au sous-arbre contenant u et deja
				      comptes au niveau inferieur)

  Suffisant pour obtenir la moitie des points. (L'approche optimale consiste a utiliser des
  Persistent Segment Trees a la place des sqrt-boxes et de faire la recherche dicho directement
  en parallele dans tous les segment trees des v(i) pour gagner un facteur log.)
*/

#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>
using namespace std;

int N;
vector<int> A;
vector< vector<int> > G;
int inf = 1000000001;


// ===== CENTROID DECOMPOSITION =====
vector<int> STSize;
vector<bool> centroided;
int CentroidRoot;
vector< vector<int> > CentroidG;
vector<int> CentroidP,CentroidLvl;

int centroid_size_dfs(int u, int u0=-1) {
  STSize[u] = 1;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0 && !centroided[*iv]) STSize[u] += centroid_size_dfs(*iv,u);
  return STSize[u];
}

int centroid(int n, int u, int u0=-1) {
  if (n==1) return u;
  int maxS = 0, maxv = -1;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0 && !centroided[*iv] && STSize[*iv]>maxS) {
      maxS = STSize[*iv];
      maxv = *iv;
    }
  if (maxS<=n/2) return u;
  else return centroid(n,maxv,u);
}

int centroidize(int u=0, int l=0) {
  int n = centroid_size_dfs(u);
  int c = centroid(n,u);
  centroided[c] = true;
  CentroidLvl[c] = l;
  for (auto iv=G[c].begin(); iv!=G[c].end(); ++iv)
    if (!centroided[*iv]) {
      int d = centroidize(*iv,l+1);
      CentroidP[d] = c;
      CentroidG[c].push_back(d);
    }
  return c;
}

void centroid_comp() {
  centroided.resize(N,false);
  STSize.resize(N);
  CentroidG.resize(N);
  CentroidP.resize(N,-1);
  CentroidLvl.resize(N,0);
  CentroidRoot = centroidize();
}
// =====  =====


// ===== SQRT DECOMP BOXES =====
typedef pair<int,int> point;

const int naive_thresh = 30;

struct SqrtBoxes {
  vector< vector< vector<point> > > box;
  vector< vector<int> > sbox;
  vector<int> boxx,boxy;
  int N,S,ymin;
  
  SqrtBoxes() {}
  //SqrtBoxes(vector<point> &V) {init(V);}

  void init(vector<point> &V);
  void insert(const point &p);
  int count(int x, int y, int K) const;
  int naive_count(int x, int y) const;
};

void SqrtBoxes::init(vector<point> &V) {
  N = V.size();
  ymin = inf;
  for (auto it=V.begin(); it!=V.end(); ++it) ymin = min(ymin,it->second);
  if (N<naive_thresh) {
    box.resize(1);
    box[0].resize(1);
    box[0][0] = V;
    sort(box[0][0].begin(),box[0][0].end());
    return;
  }
  S = (int)(sqrt(N)/3.5)+1;
  box.resize(S);
  sbox.resize(S);
  for (int i=0; i<S; ++i) {
    box[i].resize(S);
    sbox[i].resize(S,0);
  }
  // S-medians
  vector<int> X(N),Y(N);
  for (int i=0; i<N; ++i) {
    X[i] = V[i].first;
    Y[i] = V[i].second;
  }
  sort(X.begin(),X.end());
  int S0 = N/(S-1);
  for (int i=S0; i<N; i+=S0) boxx.push_back(X[i]);
  sort(Y.begin(),Y.end());
  for (int i=S0; i<N; i+=S0) boxy.push_back(Y[i]);
  // Insertion des points
  for (auto it=V.begin(); it!=V.end(); ++it) insert(*it);
  // Propagation des sommes
  for (int i=1; i<S; ++i) {
    sbox[i][0] += sbox[i-1][0];
    sbox[0][i] += sbox[0][i-1];
  }
  for (int i=1; i<S; ++i)
    for (int j=1; j<S; ++j)
      sbox[i][j] += sbox[i][j-1]+sbox[i-1][j]-sbox[i-1][j-1];
}

void SqrtBoxes::insert(const point &p) {
  // Recherche dicho des indices
  int I = distance(boxx.begin(),lower_bound(boxx.begin(),boxx.end(),p.first));
  int J = distance(boxy.begin(),lower_bound(boxy.begin(),boxy.end(),p.second));
  box[I][J].push_back(p);
  ++sbox[I][J];
}

int SqrtBoxes::count(int x, int y, int K=-1) const {
  if (x<0 || y<ymin) return 0;
  if (N<naive_thresh) return naive_count(x,y);
  int I = distance(boxx.begin(),lower_bound(boxx.begin(),boxx.end(),x));
  int J = distance(boxy.begin(),lower_bound(boxy.begin(),boxy.end(),y));
  int res = 0;
  if (I>0 && J>0) res = sbox[I-1][J-1];
  if (K>=0 && res>K) return res; // @shortcut
  // Parcours des boites a cheval
  for (int j=0; j<=J; ++j)
    for (auto it=box[I][j].begin(); it!=box[I][j].end(); ++it)
      if (it->first<=x && it->second<=y) ++res;
  if (K>=0 && res>K) return res; // @shortcut
  for (int i=0; i<I; ++i)
    for (auto it=box[i][J].begin(); it!=box[i][J].end(); ++it)
      if (it->first<=x && it->second<=y) ++res;
  return res;
}

int SqrtBoxes::naive_count(int x, int y) const {
  int res = 0;
  for (auto it=box[0][0].begin(); it!=box[0][0].end() && it->first<=x; ++it)
    if (it->second<=y) ++res;
  return res;
}
// ===== =====


vector< vector<int> > CentroidDist,CentroidPath;
vector<SqrtBoxes> CentroidBox,CentroidParBox;
vector<int> B0;

int centroid_dist(int c, int u) {
  return CentroidDist[u][CentroidLvl[c]];
}

void dfs_centroid(vector<int> &Z, int c, int u, int u0=-1, int d=0) {
  CentroidDist[u][CentroidLvl[c]] = d;
  Z.push_back(u);
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0 && CentroidLvl[*iv]>CentroidLvl[c])
      dfs_centroid(Z,c,*iv,u,d+1);
}

void precomp_dfs(int c) {
  vector<int> Z;
  dfs_centroid(Z,c,c);
  vector<point> P;
  for (auto it=Z.begin(); it!=Z.end(); ++it)
    P.push_back(make_pair(centroid_dist(c,*it),A[*it]));
  CentroidBox[c].init(P);
  if (CentroidP[c]>=0) {
    P.clear();
    for (auto it=Z.begin(); it!=Z.end(); ++it)
      P.push_back(make_pair(centroid_dist(CentroidP[c],*it),A[*it]));
    CentroidParBox[c].init(P);
  }
  for (auto it=CentroidG[c].begin(); it!=CentroidG[c].end(); ++it)
    precomp_dfs(*it);
}

void precomp() {
  CentroidDist.resize(N);
  for (int u=0; u<N; ++u) CentroidDist[u].resize(CentroidLvl[u]+1,0);
  CentroidPath.resize(N);
  for (int u=0; u<N; ++u) {
    int v = u;
    while (v>=0) {
      CentroidPath[u].push_back(v);
      v = CentroidP[v];
    }
  }
  CentroidBox.resize(N);
  CentroidParBox.resize(N);
  precomp_dfs(CentroidRoot);
}

// nb <=k (calcul coupe si on depasse) de sommets a distance <=d0 de u0 dont la valeur est <=x
int count(int u0, int d0, int x, int k) {
  int res = 0;
  // de la racine centroide vers u0 pour couper au plus vite lorsque res>k
  for (int i=(int)CentroidPath[u0].size()-1; i>=0; --i) {
    int u = CentroidPath[u0][i];
    int d = d0 - centroid_dist(u,u0);
    if (d>=0) {
      res += CentroidBox[u].count(d,x,k-res);
      if (res>k) return res;
      if (i>0) {
	int v = CentroidPath[u0][i-1];
	res -= CentroidParBox[v].count(d,x);
      }
    }
  }
  return res;
}

// nb total de sommets a distance <=d0 de u0 dont la valeur est <=x
int count_total(int u0, int d0, int x) {
  int res = 0;
  for (int i=(int)CentroidPath[u0].size()-1; i>=0; --i) {
    int u = CentroidPath[u0][i];
    int d = d0 - centroid_dist(u,u0);
    res += CentroidBox[u].count(d,x);
    if (i>0) {
      int v = CentroidPath[u0][i-1];
      res -= CentroidParBox[v].count(d,x);
    }
  }
  return res;
}

int get_kth(int u, int d, int k) {
  // optimisation des bornes de la recherche dichotomique
  int c0 = count_total(u,d,inf);
  if (c0<k) return inf;
  int l = B0[k-1], r = B0[N-1-(c0-k)];
  while (l<r) {
    int m = (l+r)/2;
    int c = count(u,d,m,k);
    if (c<k) l = m+1;
    else r = m;
  }
  return l;
}

// compression/renumerotation des valeurs
unordered_map<int,int> Renum;
vector<int> InvRenum;
void renum() {
  vector<int> B = A;
  sort(B.begin(),B.end());
  for (int i=0; i<N; ++i) {
    if (i==0 || B[i]!=B[i-1]) {
      Renum[B[i]] = Renum.size();
      InvRenum.push_back(B[i]);
    }
    B0.push_back(Renum[B[i]]);
  }
  for (int i=0; i<N; ++i) A[i] = Renum[A[i]];
  inf = Renum.size();
}


int main() {
  scanf("%d",&N);
  A.resize(N);
  for (int i=0; i<N; ++i) scanf("%d",&A[i]);
  renum();
  G.resize(N);
  for (int i=0; i<N-1; ++i) {
    int u,v;
    scanf("%d %d",&u,&v); --u; --v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  centroid_comp();
  precomp();
  int Q;
  scanf("%d",&Q);
  for (int q=0; q<Q; ++q) {
    int u,d,k;
    scanf("%d %d %d",&u,&d,&k); --u;
    int res = get_kth(u,d,k);
    if (res==inf) res = -1;
    else res = InvRenum[res];
    printf("%d\n",res);
  }
  return 0;
}
