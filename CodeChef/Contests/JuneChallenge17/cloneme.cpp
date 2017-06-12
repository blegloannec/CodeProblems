#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

/*
  Approche offline. On pre-calcule les sommes, xor et produits modulo
  des prefixes pour avoir ces valeurs sur un intervalle en O(1).
  On considere 2 intervalles egaux si ces trois valeurs sont identiques.
  Pour les differences d'un element, on remarque que si deux intervalles
  ont un seul indice ou ils different, alors notons a et b les elements
  distincts, les 2 sommes sont donc s+a et s+b ou s est la somme commune
  des autres elements (identiques) et les produits sont ka et kb ou
  k est le produit des autres elements. En soustrayant les sommes on
  obtient a-b, en soustrayant les produits k(a-b), on peut donc en
  deduire k, et connaissant les produits en deduire a et b (modulo, mais
  en choisissant un modulo plus grand que les valeurs possibles du tableau
  on obtient les "vraies" valeurs candidates de a et b).
  On va alors verifier cette analyse : on verifie que les sommes respectives 
  -a et -b sont egales, idem pour les xor et si c'est le cas on va mettre
  les requetes en question en attente pour les traiter de facon offline
  afin de verifier que les elements a et b sont bien presents dans les
  intervalles en question et qu'ils ont le meme rang dans les intervalles
  tries.
  Pour ca on balaye l'ensemble de nombres de gauche a droite en comptant
  les nombres vus dans un arbre de Fenwick servant d'ensemble de buckets.
  Pour chaque intervalle [l,r] mis en attente avec la valeur candidate x.
  le nombre nx de x dans l'intervalle est egal a la difference entre le nb
  de x dans l'arbre apres l'instant r et le nb de x avant l'instant l.
  On verifie qu'il y en a au moins 1.
  Et l'intervalle des rangs des nx elements x dans l'ensemble trie
  s'obtient de la meme facon a partir du nb d'elements <=x avant l'instant l
  et du nb d'elements <=x apres l'instant r dans l'arbre.
  Pour chaque paire d'intervalles associes a la meme requete, on verifie
  enfin que ces intervalles de rangs calcules pour les candidats respectifs
  s'intersectent en 1 point.
*/

typedef long long ent;

struct inter {
  int a,id,x,q;
  inter(int a, int id, int x, int q) : a(a), id(id), x(x), q(q) {}
  bool operator<(const inter &J) {
    return a<J.a;
  }
};

const ent M = 1000000007;

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

ent inv_mod(ent a, ent n=M) {
  ent u,v;
  bezout(a,n,u,v);
  return (u+n)%n;
}

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;
  ent operator[](int i) const;

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

ent Fenwick::prefix_sum(int i) const {
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}

ent Fenwick::operator[](int i) const {
  return prefix_sum(i)-prefix_sum(i-1);
}

int main() {
  int T,N,Q;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    scanf("%d %d",&N,&Q);
    vector<ent> A(N+1,0),S(N+1,0),P(N+1,1),X(N+1,0);
    for (int i=1; i<=N; ++i) {
      scanf("%lld",&A[i]);
      S[i] = S[i-1]+A[i];
      P[i] = (P[i-1]*A[i])%M;
      X[i] = X[i-1]^A[i];
    }
    vector<bool> res(Q);
    vector<inter> Il,Ir;
    int id = 0;
    for (int q=0; q<Q; ++q) {
      int a,b,c,d;
      scanf("%d %d %d %d",&a,&b,&c,&d);
      ent Sab = S[b]-S[a-1];
      ent Scd = S[d]-S[c-1];
      ent Pab = (P[b]*inv_mod(P[a-1]))%M;
      ent Pcd = (P[d]*inv_mod(P[c-1]))%M;
      ent Xab = X[b]^X[a-1];
      ent Xcd = X[d]^X[c-1];
      if (Sab==Scd && Pab==Pcd && Xab==Xcd) res[q] = true;
      else {
	ent z = (Sab-Scd + M)%M;
	ent k = (((Pab-Pcd)%M * inv_mod(z))%M + M)%M;
	ent xab = (Pab*inv_mod(k))%M;
	ent xcd = (Pcd*inv_mod(k))%M;
	if (xab<1 || xcd<1 || xab>100000 || xcd>100000 || Sab-xab!=Scd-xcd || (Xab^xab)!=(Xcd^xcd)) res[q] = false;
	else { // appartenance a verifier
	  res[q] = true;
	  Il.push_back(inter(a,id,xab,q));
	  Ir.push_back(inter(b,id,xab,q));
	  ++id;
	  Il.push_back(inter(c,id,xcd,q));
	  Ir.push_back(inter(d,id,xcd,q));
	  ++id;
	}
      }
    }
    sort(Il.begin(),Il.end());
    sort(Ir.begin(),Ir.end());
    int il = 0, ir = 0;
    Fenwick cpt(100000);
    vector<int> inter_cpt(id,0), inter_delta(id,0);
    vector<bool> finish(id,false);
    for (int i=1; i<=N; ++i) {
      while (il<id && Il[il].a==i) {
	inter_cpt[Il[il].id] = -cpt[Il[il].x];
	inter_delta[Il[il].id] = -cpt.prefix_sum(Il[il].x);
	++il;
      }
      cpt.add(A[i]);
      while (ir<id && Ir[ir].a==i) {
	int id0 = Ir[ir].id;
	inter_cpt[id0] += cpt[Ir[ir].x];
	inter_delta[id0] += cpt.prefix_sum(Ir[ir].x);
	finish[id0] = true;
	if (inter_cpt[id0]<=0) res[Ir[ir].q] = false;
	int id1 = id0%2==0 ? id0+1 : id0-1;
	if (res[Ir[ir].q] && finish[id1]) {
	  int l0 = inter_delta[id0]-inter_cpt[id0];
	  int r0 = inter_delta[id0]-1;
	  int l1 = inter_delta[id1]-inter_cpt[id1];
	  int r1 = inter_delta[id1]-1;
	  if (max(l0,l1)>min(r0,r1)) res[Ir[ir].q] = false;
	}
	++ir;
      }
    }
    for (int q=0; q<Q; ++q)
      if (res[q]) printf("YES\n");
      else printf("NO\n");
  }
  return 0;
}
