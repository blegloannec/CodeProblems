#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ent;
ent P;
int N;
vector<ent> A,S,F;

ent expmod(ent x, ent n, ent m) {
  if (!n) return 1;
  if (!(n&1)) return expmod((x*x)%m,n>>1,m);
  return (x*expmod((x*x)%m,n>>1,m))%m;
}

ent invmod(ent x) {
  return expmod(x,P-2,P);
}

ent binom(int n, int p) {
  return (F[n]*((invmod(F[p])*invmod(F[n-p]))%P))%P;
}

void precomp_fact() {
  F.resize(N+1,1);
  for (int i=2; i<=N; ++i) F[i] = (i*F[i-1]) % P;
}

int main() {
  cin >> P;
  cin >> N;
  precomp_fact();
  A.resize(N);
  for (int i=0; i<N; ++i) cin >> A[i];
  sort(A.begin(),A.end());  // on trie
  S = A;
  int dup = 1;
  ent denom = 1; /* on calcule le produit des factorielles des multiplicites
		    des valeurs de A car la question porte sur le nb de
		    permutations *de A* (pas des indices) */
  for (int i=1; i<N; ++i) {
    S[i] = (S[i-1]+S[i]) % P;  // somme prefixe de A trie
    if (A[i]==A[i-1]) ++dup;
    else {
      denom = (denom*F[dup]) % P;
      dup = 1;
    }
  }
  denom = invmod((denom*F[dup])%P);
  int Q;
  cin >> Q;
  for (int q=0; q<Q; ++q) {
    int M;
    cin >> M;
    // k l'indice du premier element >M dans A trie
    int k = distance(A.begin(),upper_bound(A.begin(),A.end(),M));
    ent s = (k>0 ? S[k-1] : 0);
    ent res = 0;
    if (k>0) {
      /* chaque valeur A[i] pour i<k dans A trie a la meme contribution
	 au resultat : le nb de permutations dans lesquelles cette valeur
	 est placee avant les N-k valeurs >M (les A[k:])
	 i.e. binom(N,N-k+1)       * (k-1)!         * (N-k)!
	      choix des positions    permutation      permutation des A[k:]
	      de A[i] et des A[k:]   des k-1 autres
              (A[i] sera place a     elements
	       la premiere de ces
	       positions)
      */
      res = (s*((binom(N,N-k+1)*((F[k-1]*F[N-k])%P))%P))%P;
      res = (res*denom)%P;
    }
    cout << res << endl;
  }
  return 0;
}
