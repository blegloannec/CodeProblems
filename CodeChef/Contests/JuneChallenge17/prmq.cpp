#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

/*
  Approche offline, on stocke les bornes L et R de chaque
  requete et on les trie.
  On balaye A de gauche a droite, chaque nouveau nombre est
  factorise et les multiplicites de chacun de ses facteurs premiers
  sont ajoutees, a l'indice du facteur, dans un arbre de Fenwick.
  Chaque requete d'intervalle [L,R] sur les nombres et [X,Y] sur les
  facteurs est egale a la somme sur [X,Y] de la structure apres l'instant R
  - la meme somme avant l'instant L.
*/

typedef long long ent;
typedef pair<int,int> couple;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;
  ent range(int i, int j) const;

  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  //assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}

ent Fenwick::range(int i, int j) const {
  return prefix_sum(j)-prefix_sum(i-1);
}

const int M = 1000001;
vector<bool> P(M,true);
vector<int> F(M,1);

void sieve_smallest_factor() {
  P[0] = P[1] = false;
  for (int i=2; i<M; ++i)
    if (P[i]) {
      F[i] = i;
      for (int k=2*i; k<M; k+=i)
	if (P[k]) {
	  P[k] = false;
	  F[k] = i;
	}
    }
}

void decomp(int n, vector<couple> &D) {
  int p = F[n];
  n /= p;
  int m = 1;
  while (n%p==0) {
    n /= p;
    ++m;
  }
  D.push_back(couple(p,m));
  if (n>1) decomp(n,D);
}

int main() {
  sieve_smallest_factor();
  int N,Q;
  scanf("%d",&N);
  vector<int> A(N);
  for (int i=0; i<N; ++i) scanf("%d",&A[i]);
  scanf("%d",&Q);
  vector<couple> L,R;
  vector<int> X(Q),Y(Q);
  for (int i=0; i<Q; ++i) {
    int l,r;
    scanf("%d %d %d %d",&l,&r,&X[i],&Y[i]);
    L.push_back(couple(l,i));
    R.push_back(couple(r,i));
  }
  sort(L.begin(),L.end());
  sort(R.begin(),R.end());
  int il = 0, ir = 0;
  Fenwick F(M);
  vector<ent> res(Q);
  for (int i=1; i<=N; ++i) {
    // on traite les intervalles ayant L = i
    while (il<Q && L[il].first==i) {
      int q = L[il].second;
      res[q] = -F.range(X[q],Y[q]);
      ++il;
    }
    // on met a jour l'arbre de Fenwick en y ajoutant les multiplicites
    // des facteurs du nouvel element
    vector<couple> D;
    decomp(A[i-1],D);
    for (vector<couple>::iterator it=D.begin(); it!=D.end(); ++it)
      F.add(it->first,it->second);
    // on traite les intervalles ayant R = i
    while (ir<Q && R[ir].first==i) {
      int q = R[ir].second;
      res[q] += F.range(X[q],Y[q]);
      ++ir;
    }
  }
  for (int i=0; i<Q; ++i) printf("%lld\n",res[i]);
  return 0;
}
