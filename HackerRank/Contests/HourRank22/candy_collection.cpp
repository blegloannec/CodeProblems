#include <cstdio>
#include <vector>
using namespace std;

/*
  On numerote les boites de 0 a n-1.
  Soit C(n) = cout minimal du decoupage des n premieres boites
  Soit K(n) = le plus petit k tel que les boites de k a n ne
              contiennent pas 2 fois la meme couleur
  On a C(n+1) = min( C(k) + OR(k,n), K(n) <= k <= n )
  pour OR(k,n) le OU des boites numerotees k a n.
  Ce calcul se fait naivement en O(n^2) mais :
   - les K(n) sont croissants et l'on peut utiliser une technique de double
     pointeur pour tous les calculer en O(n) ;
   - on peut utiliser un arbre de segments contenant a l'instant n toutes les
     valeurs C(k) + OR(k,n) et obtenir le min sur [K(n),n] en O(log n) ;
  La seule difficulte est la mise a jour de l'arbre lors du passage de n a n+1.
  L'idee est de traiter independemment les bits : si le i-ieme bit de T[n]
  vaut 1 et que l'on connait last1[i] = le plus grand indice i0<n tel que
  le i-eme bit de T[i0] vaut 1 (ce que l'on peut retenir a la volee), alors
  il faut passer a 1 le i-eme bit des valeurs des OR(k,n) pour i0+1<=k<n,
  autrement dit ajouter 2^i aux valeurs de l'intervalle [i0+1,n-1].
*/

typedef int elem;

struct LazySegmentTree {
  const elem NEUTRAL = 1000000000; // neutre
  unsigned int N;
  vector<elem> S,L;
  vector<bool> L0;

  // operation utilisee, e.g. min, +, *, etc
  static inline elem op(elem a, elem b) {
    return min(a,b);
  }

  // operation iteree n fois
  // a pour min, n*a pour +, a^n pour *
  static inline elem iter_op (elem a, int n) {
    return a;
  }

  // operation de mise a jour (via set() et range_set())
  // a pour un remplacement, a0+a pour addition
  static inline elem up_op (elem a0, elem a) {
    return a0+a;
  }
  
  LazySegmentTree(const vector<elem> &T) {
    N = 1;
    while (N<T.size()) N <<= 1;
    S.resize(2*N,NEUTRAL);
    L.resize(N,NEUTRAL); // lazy fields
    L0.resize(N,false);
    // les feuilles sont les elements >=N
    for (unsigned int i=0; i<T.size(); ++i) S[N+i] = T[i];
    // les noeuds internes sont les elements de 1 a N-1
    for (int p=N-1; p>0; --p) S[p] = op(S[2*p],S[2*p+1]);
  }

  void _update_lazy_field(int p, elem v) {
    // assert(p<(int)N)
    if (L0[p]) // il y a deja une mise a jour en attente en p
      L[p] = up_op(L[p],v);
    else {
      L0[p] = true;
      L[p] = v;
    }
  }
  
  void _propagate(int p, int span) {
    //assert(p<(int)N && L0[p]);
    // propagation de la lazy value de p,
    // mise a jour des valeurs des 2 fils
    int D = iter_op(L[p],span/2);
    S[2*p] = up_op(S[2*p],D);
    S[2*p+1] = up_op(S[2*p+1],D);
    if (2*p<(int)N) {
      // mise a jour des lazy values des 2 fils
      _update_lazy_field(2*p,L[p]);
      _update_lazy_field(2*p+1,L[p]);
    }
    L0[p] = false;
  }

  void _lazy_set_range(int p, int start, int span, int i, int j, elem v) {
    if (start+span<=i || j<=start) return;
    else if (i<=start && start+span<=j) {
      // mise a jour des valeurs de p
      S[p] = up_op(S[p],iter_op(v,span));
      if (p<(int)N) _update_lazy_field(p,v);
    }
    else {
      if (p<(int)N && L0[p]) _propagate(p,span);
      _lazy_set_range(2*p,start,span/2,i,j,v);
      _lazy_set_range(2*p+1,start+span/2,span/2,i,j,v);
      S[p] = op(S[2*p],S[2*p+1]);
    }
  }
  
  void set_range(int i, int j, elem v) {
    _lazy_set_range(1,0,N,i,j+1,v);
  }

  // returns the op in t in the indexes [i,j) intersected
  // with [start,start+span)
  elem _range(int p, int start, int span, int i, int j) {
    if (start+span<=i || j<=start) return NEUTRAL;
    if (i<=start && start+span<=j) return S[p];
    if (p<(int)N && L0[p]) _propagate(p,span);
    elem left = _range(2*p,start,span/2,i,j);
    elem right = _range(2*p+1,start+span/2,span/2,i,j);
    return op(left,right);
  }
  
  // returns op{t[i], t[i+1], ..., t[j]}
  elem range(int i, int j) {
    return _range(1,0,N,i,j+1);
  }

  elem get(int i) {
    return range(i,i);
  }

  void set(int i, elem v) {
    set_range(i,i,v);
  }
};

int main() {
  int n;
  scanf("%d",&n);
  vector<int> T(n),V(n),Cpt(1000001,0),K(n);
  for (int i=0; i<n; ++i) scanf("%d",&T[i]);
  for (int i=0; i<n; ++i) scanf("%d",&V[i]);
  // Calcul de K, O(n)
  int j = 0;
  for (int i=0; i<n; ++i) {
    while (j<i && Cpt[T[i]]>0) --Cpt[T[j++]];
    K[i] = j;
    ++Cpt[T[i]];
  }
  // Calcul de C, O(n*B log n)
  const int B = 20;
  vector<int> C(n),last1(B,-1);;
  LazySegmentTree ST(V);
  for (int i=0; i<n; ++i) {
    ST.set(i,(i>0 ? C[i-1] : 0));
    for (int b=0; b<B; ++b)
      if (V[i]&(1<<b)) {
	if (last1[b]+1<=i-1)
	  ST.set_range(last1[b]+1,i-1,1<<b);
	last1[b] = i;
      }
    C[i] = ST.range(K[i],i);
  }
  printf("%d\n",C[n-1]);
  return 0;
}
