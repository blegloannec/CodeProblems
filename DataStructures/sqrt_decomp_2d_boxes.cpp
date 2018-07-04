#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

/*
  Etant donnes N points, et pour S = sqrt(N)/D, on fabrique une
  table de S x S boites pour les ranger (en moyenne D^2 points par boite
  en supposant une "homogeneite suffisante" des points dans l'espace, sachant
  qu'on utilise des quantiles selon x et y pour delimiter les boites)
  et repondre a des requetes (x,y) consistant a compter (ou n'importe quel
  autre type de somme, etc) le nb de points (a,b) dans la structure
  verifiant a<=x et b<=y en O(S*D^2) = O(sqrt(N)*D).
  En theorie, D = 1 est optimal, choisir D > 1 assez petit est souvent
  un peu plus efficace.
*/

// ===== SQRT DECOMP BOXES =====
typedef int xtype;
typedef int ytype;
typedef int ctype; // type pour le denombrement / somme
typedef pair<xtype,ytype> point;

struct SqrtBoxes {
  const int naive_thresh = 30;  /* taille en dessous de laquelle on se
				 contente d'une simple liste triee en x */
  const float D = 3.5;          // pour S = sqrt(N)/D
  
  vector< vector< vector<point> > > box;
  vector< vector<ctype> > sbox;
  vector<xtype> boxx;
  vector<ytype> boxy;
  int N,S;
  
  SqrtBoxes() {}
  SqrtBoxes(vector<point> &V) {init(V);}

  void init(vector<point> &V);
  void insert(const point &p);
  ctype count(xtype x, ytype y) const;
  ctype naive_count(xtype x, ytype y) const;
};

void SqrtBoxes::init(vector<point> &V) {
  N = V.size();
  if (N<naive_thresh) {
    box.resize(1);
    box[0].resize(1);
    box[0][0] = V;
    sort(box[0][0].begin(),box[0][0].end());
    return;
  }
  S = (int)(sqrt(N)/D)+1;
  box.resize(S);
  sbox.resize(S);
  for (int i=0; i<S; ++i) {
    box[i].resize(S);
    sbox[i].resize(S,0);
  }
  // S-quantiles
  vector<xtype> X(N);
  vector<ytype> Y(N);
  for (int i=0; i<N; ++i) {
    X[i] = V[i].first;
    Y[i] = V[i].second;
  }
  sort(X.begin(),X.end());
  //int S0 = (N+S-1)/S;
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

ctype SqrtBoxes::count(xtype x, ytype y) const {
  if (N<naive_thresh) return naive_count(x,y);
  int I = distance(boxx.begin(),lower_bound(boxx.begin(),boxx.end(),x));
  int J = distance(boxy.begin(),lower_bound(boxy.begin(),boxy.end(),y));
  ctype res = 0;
  if (I>0 && J>0) res = sbox[I-1][J-1];
  // Parcours des boites a cheval
  for (int j=0; j<=J; ++j)
    for (auto it=box[I][j].begin(); it!=box[I][j].end(); ++it)
      if (it->first<=x && it->second<=y) ++res;
  for (int i=0; i<I; ++i)
    for (auto it=box[i][J].begin(); it!=box[i][J].end(); ++it)
      if (it->first<=x && it->second<=y) ++res;
  return res;
}

ctype SqrtBoxes::naive_count(xtype x, ytype y) const {
  ctype res = 0;
  for (auto it=box[0][0].begin(); it!=box[0][0].end() && it->first<=x; ++it)
    if (it->second<=y) ++res;
  return res;
}
// ===== =====


int main() {
  return 0;
}
