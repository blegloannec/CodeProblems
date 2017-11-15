#include <cstdio>
#include <vector>
using namespace std;

/*
  Une approche par segment tree sur le produit modulo est trop lente ici
  (et les sparse tables non appropriees a cause du recouvrement, le produit
  n'etant pas idempotent).

  Pour traiter le pb des Ai = 0, on calcule les sommes cumulees du
  nb de 0 dans A (on sait alors en O(1) si un intervalle contient 0).
  Dans la suite, on remplace alors les Ai = 0 par des 1.
  Pour P = Prod_k pk^mk  (decomposition primale),
  on ecrit les Ai = ai Prod_k pk^bki avec ai>0 premier avec P (donc inversible).
  On pre-calcule les produits prefixes (mod P) des ai ainsi que leurs inverses
  modulaires et les sommes prefixes des bki pour tout k.
  Le produit sur un intervalle [l,r] (ne contenant pas 0) est alors :
    ar * a(l-1)^(-1) * Prod_k pk^(bkr-bk(l-1))  mod P
  En pre-calculant "assez loin" les puissances des pk modulo, on peut esperer
  avoir "la plupart" de ces puissances en O(1) et ainsi repondre a chaque
  requete en O(nb de facteurs premiers distincts de P).
  C'est <= 9 ici (pour P <= 10^9), la ou un facteur log2 n est <= 30 (et est
  de plus clairement un majorant du nb de facteurs premiers distincts).

  Cette methode implementee efficacement et optimisee passe tout juste
  (a 50 ms pres pour le 1er testcase du 3eme subset)...
*/

typedef long long ent;

const int SMAX = 1000002;
const int QMAX = 20000000/64+3;
ent A[SMAX],Ainv[SMAX],B[QMAX];
int Z[SMAX];
int M[SMAX][20];
const int EMAX = 2000000;
ent E[20][EMAX];

ent expmod(ent a, ent b, ent q) {
  ent res = 1;
  while (b) {
    if (b&1) {
      res *= a;
      if (res>=q) res %= q;
    }
    a *= a;
    if (a>=q) a %= q;
    b >>= 1;
  }
  return res;
}

ent bezout(ent a, ent b, ent &u, ent &v) {
  if (b==0) {
    u = 1;
    v = 0;
    return a;
  }
  ent u1,v1;
  ent g = bezout(b,a%b,u1,v1);
  u = v1;
  v = u1-(a/b)*v1;
  return g;
}

ent inv_mod(ent a, ent n) {
  ent u,v;
  bezout(a,n,u,v);
  if (u<0) u += n;
  return u;
}

void decomp(ent n, vector<ent> &D) {
  for (int d=2; d*d<=n; ++d) {
    int m = 0;
    while (n%d==0) {
      n /= d;
      ++m;
    }
    if (m>0) D.push_back(d);
  }
  if (n>1) D.push_back(n);
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    ent P;
    int N,Q,E0;
    scanf("%d %lld %d",&N,&P,&Q);
    vector<ent> D;
    decomp(P,D);
    int SD = D.size();
    if (D[0]<P) {
      E0 = EMAX/SD;
      for (int f=0; f<SD; ++f) {
	E[f][0] = 1;
	for (int i=1; i<E0; ++i) {
	  E[f][i] = E[f][i-1]*D[f];
	  if (E[f][i]>=P) E[f][i] %= P;
	}
      }
    }
    A[0] = Ainv[0] = 1;
    Z[0] = 1;
    for (int f=0; f<SD; ++f) M[0][f] = 0;
    for (int i=1; i<=N; ++i) {
      scanf("%lld",&A[i]);
      A[i] %= P;
      Z[i] = Z[i-1];
      if (A[i]==0) {
	A[i] = 1;
	++Z[i];
      }
      for (int f=0; f<SD; ++f) {
	int m = 0;
	while (A[i]%D[f]==0) {
	  A[i] /= D[f];
	  ++m;
	}
	M[i][f] = m + M[i-1][f];
      }
      A[i] *= A[i-1];
      if (A[i]>=P) A[i] %= P;
      Ainv[i] = inv_mod(A[i],P);
    }
    int S = Q/64+2;
    for (int i=0; i<S; ++i) scanf("%lld",&B[i]);
    ent x=0,L,R;
    for (int i=0; i<Q; ++i) {
      if (i%64==0) {
	L = B[i/64]+x;
	R = B[i/64+1]+x;
      }
      else {
	L += x;
	R += x;
      }
      if (L>=N) L %= N;
      if (R>=N) R %= N;
      if (L>R) swap(L,R);
      if (Z[R+1]-Z[L]>0) x = 0;
      else {
	x = A[R+1]*Ainv[L];
	if (x>=P) x %= P;
	for (int f=0; f<SD; ++f) {
	  int p = M[R+1][f]-M[L][f];
	  if (p>0) {
	    if (p<E0) x *= E[f][p];
	    else x *= expmod(D[f],p,P);
	    if (x>=P) x %= P;
	  }
	}
      }
      x = (x==P-1 ? 0 : x+1);
    }
    printf("%lld\n",x);
  }
  return 0;
}
