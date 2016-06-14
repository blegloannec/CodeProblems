#include <iostream>
#include <cmath>
//#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ent;
typedef pair<ent,int> couple;
typedef pair<double,ent> limite;

/*
// ===== QUADTREE =====
// Trop lent, meme avec homogeneisation des donnees dans l'espace
// homogeneisation des donnees selon Y
#define RY(Y) (exp(5*(Y)))

struct quadtree {
  limite borninf,bornsup,point;
  ent sum;
  bool leaf;
  quadtree *sw,*se,*ne,*nw;
  // new leaf
  quadtree(limite bi, limite bs, limite p) : borninf(bi), bornsup(bs), point(p), sum(p.first), leaf(true), sw(NULL), se(NULL), ne(NULL), nw(NULL) {}
  // init tree
  quadtree(limite bi, limite bs) : borninf(bi), bornsup(bs), point(limite((bi.first+bs.first)/2,(bi.second+bs.second)/2)), sum(0L), leaf(false), sw(NULL), se(NULL), ne(NULL), nw(NULL) {}
};

void qt_insert(quadtree *t, const limite &p) {
  t->sum += p.first;
  if (t->leaf) {
    if (p == t->point) return;
    limite p0 = t->point;
    t->point = limite((t->borninf.first+t->bornsup.first)/2,(t->borninf.second+t->bornsup.second)/2);
    t->leaf = false;
    t->sum -= p.first;
    int mult = t->sum/p0.first;
    for (int i=0; i<mult; ++i) qt_insert(t,p0);
    qt_insert(t,p);
  }
  else {
    if (p.first < t->point.first && p.second < t->point.second) {
      if (t->sw==NULL) t->sw = new quadtree(t->borninf,t->point,p);
      else qt_insert(t->sw,p);
    }
    else if (p.first < t->point.first && p.second >= t->point.second) {
      if (t->nw==NULL) t->nw = new quadtree(limite(t->borninf.first,t->point.second),limite(t->point.first,t->bornsup.second),p);
      else qt_insert(t->nw,p);
    }
    else if (p.first >= t->point.first && p.second < t->point.second) {
      if (t->se==NULL) t->se = new quadtree(limite(t->point.first,t->borninf.second),limite(t->bornsup.first,t->point.second),p);
      else qt_insert(t->se,p);
    }
    else {
      if (t->ne==NULL) t->ne = new quadtree(t->point,t->bornsup,p);
      else qt_insert(t->ne,p);
    }
  }
}

ent qt_find(quadtree *t, const limite &p) {
  if (t==NULL) return 0L;
  //assert(p.first >= t->borninf.first && p.second >= t->borninf.second);
  if (t->leaf) {
    if (p.first > t->point.first && p.second >= t->point.second)
      return t->sum;
    return 0L;
  }
  if (p.first >= t->bornsup.first && p.second >= t->bornsup.second)
    return t->sum;
  if (p.first <= t->point.first) {
    if (p.second <= t->point.second) return qt_find(t->sw,p);
    return qt_find(t->nw,p)+qt_find(t->sw,p);
  }
  else {
    if (p.second <= t->point.second) return qt_find(t->se,p)+qt_find(t->sw,p);
    return (t->sw!=NULL?t->sw->sum:0L)+qt_find(t->ne,p)+qt_find(t->nw,p)+qt_find(t->se,p);
  }
}

// Dessin SVG de l'arbre
#define FX(X) (((double)(X))/100.)
#define FY(Y) (((Y)-0.6)*1000.)

void qt_print(quadtree *t) {
  if (t!=NULL) {
    if (t->leaf)
      cout << "<circle cx=\"" << FX(t->point.first) << "\" cy=\"" << FY(t->point.second) << "\" r=\"1\" fill=\"blue\" />" << endl;
    cout << "<rect x=\"" << FX(t->borninf.first) << "\" y=\"" << FY(t->borninf.second) << "\" width=\"" << FX(t->bornsup.first-t->borninf.first) << "\" height=\"" << FY(t->bornsup.second)-FY(t->borninf.second) << "\" stroke=\"red\" fill-opacity=\"0\" />" << endl;
    qt_print(t->sw);
    qt_print(t->se);
    qt_print(t->ne);
    qt_print(t->nw);
  }
}

// BUG QQPART DANS LE CALCUL DES SOMMES LORS DES INSERTIONS
// RECALCUL CI-DESSOUS
ent qt_sum(quadtree *t) {
  if (t==NULL) return 0L;
  if (t->leaf) return t->sum;
  ent res = qt_sum(t->sw)+qt_sum(t->se)+qt_sum(t->ne)+qt_sum(t->nw);
  //assert(t->sum==res);
  t->sum = res;
  return res;
}
*/


// ===== CRIBLE TRIPLETS =====
const int C = 100000;
vector<bool> P = vector<bool>(C,true);
vector<ent> Rad = vector<ent>(C,1L);
// couples (rad[x],x) tries
vector<couple> SRad = vector<couple>(C);
// valeurs (c, r limite) pour chaque triplet
vector<limite> V;
//quadtree Q = quadtree(limite(0,0.),limite(C,RY(1.5)));

void sieve() {
  P[0] = P[1] = false;
  for (int i=1; i<C; ++i) {
    SRad[i].first = 1L;
    SRad[i].second = i;
  }
  for (int i=2; i<C; ++i)
    if (P[i]) {
      Rad[i] = i;
      SRad[i].first = i;
      for (int j=2*i; j<C; j+=i) {
	Rad[j] *= i;
	SRad[j].first *= i;
	P[j] = false;
      }
    }
}

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

void precomp(int L, double r) {
  // on itere sur c
  for (int c=3; c<L; ++c) {
    double cr = pow(c,r);
    double scrr = sqrt(cr/Rad[c]);
    if (2*Rad[c] >= cr) continue;
    // on veut rad(a)*rad(b) < c^r/rad(c)
    // donc parmi {rad(a),rad(b)} l'un des deux
    // au moins (possiblement les 2) est plus petit
    // que sqrt(c^r/rad(c))
    // on itere sur a (ou b) suivant les rad croissants
    for (int ia=1; ia<C; ++ia) {
      int a = SRad[ia].second;
      // si rad(a) >= sqrt(c^r/rad(c)) on coupe tout
      if (Rad[a] >= scrr) break;
      if (a>=c) continue;
      int b = c-a;
      if (a==b) continue;
      // si (a,b) dans le mauvais sens (ie b<a) et
      // si rad(b) < sqrt(c^r/rad(c)), alors (b,a) sera
      // considere lors des iterations sur a
      // on saute donc ici sinon doublon
      if (b<a && Rad[b]<scrr) continue;
      ent rad = Rad[a]*Rad[b]*Rad[c];
      if (rad<cr && gcd(a,b)==1) {
	V.push_back(limite(log(rad)/log(c),c));
	//qt_insert(&Q,limite(c,RY(log(rad)/log(c))));
      }
    }
  }
}


// ===== SQRT DECOMP BOXES =====
vector<limite> box[300][300];
ent sbox[300][300];
vector<ent> boxx;
vector<double> boxy;
int S;

void insert_box(const limite &p) {
  // Recherche dicho des indices
  int I = distance(boxx.begin(),lower_bound(boxx.begin(),boxx.end(),p.second));
  int J = distance(boxy.begin(),lower_bound(boxy.begin(),boxy.end(),p.first));
  box[I][J].push_back(p);
  sbox[I][J] += p.second;
}

ent find_box(ent L, double r) {
  int I = distance(boxx.begin(),lower_bound(boxx.begin(),boxx.end(),L));
  int J = distance(boxy.begin(),lower_bound(boxy.begin(),boxy.end(),r));
  ent res = 0L;
  if (I>0 && J>0)
    res = sbox[I-1][J-1];
  // Parcours des boites a cheval
  for (int j=0; j<=J; ++j)
    for (int k=0; k<(int)box[I][j].size() && box[I][j][k].first<=r; ++k)
      if (box[I][j][k].second<L) res += box[I][j][k].second;
  for (int i=0; i<I; ++i)
    for (int k=0; k<(int)box[i][J].size() && box[i][J][k].first<=r; ++k)
      if (box[i][J][k].second<L) res += box[i][J][k].second;
  return res;
}

void build_boxes() {
  S = (int)sqrt(V.size())+1;
  for (int i=0; i<S; ++i)
    for (int j=0; j<S; ++j)
      sbox[i][j] = 0L;
  // S-medians pour X
  for (int i=S; i<(int)V.size(); i+=S)
    boxx.push_back(V[i].second);
  // S-medians pour Y
  sort(V.begin(),V.end());
  for (int i=S; i<(int)V.size(); i+=S)
    boxy.push_back(V[i].first);
  // Insertion des points
  for (vector<limite>::iterator it=V.begin(); it!=V.end(); ++it)
    insert_box(*it);
  // Propagation des sommes
  for (int i=1; i<S; ++i) {
    sbox[i][0] += sbox[i-1][0];
    sbox[0][i] += sbox[0][i-1];
  }
  for (int i=1; i<S; ++i)
    for (int j=1; j<S; ++j)
      sbox[i][j] += sbox[i][j-1]+sbox[i-1][j]-sbox[i-1][j-1];
}


// ===== MAIN =====
int main() {
  sieve();
  sort(SRad.begin(),SRad.end());
  precomp(C,1.5);
  
  /* // Impression des points pour debug plot
  cout << V.size() << endl;
  for (vector<limite>::iterator it=V.begin(); it!=V.end(); ++it)
    cout << it->first << ' ' << RY(it->second) << endl;
  return 0;
  */

  /* // Impression de l'arbre pour debug
  for (int i=0; i<500; ++i) qt_insert(&Q,V[100*i]);
  cout << "<svg width=\"1000\" height=\"900\">" << endl;
  qt_print(&Q);
  cout << "</svg>" << endl;
  return 0;
  */
  
  int T,L;
  double r;
  cin >> T;

  /* // Solution lente pour peu de testcases
  for (int t=0; t<T; ++t) {
    cin >> r >> L;
    ent res = 0;
    for (vector<limite>::iterator it=V.begin(); it!=V.end() && it->first<L; ++it)
      if (it->second<=r) res += it->first;
    cout << res << endl;
  }
  */

  /* // Solution quadtree trop lente
  for (vector<limite>::iterator it=V.begin(); it!=V.end(); ++it)
    qt_insert(&Q,*it);
  qt_sum(&Q);
  for (int t=0; t<T; ++t) {
    cin >> r >> L;
    cout << qt_find(&Q,limite(L,RY(r))) << endl;
  }
  */

  // BOITES
  build_boxes();
  for (int t=0; t<T; ++t) {
    cin >> r >> L;
    cout << find_box(L,r) << endl;
  }
  return 0;
}
