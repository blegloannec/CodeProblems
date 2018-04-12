/*
  Jeu combinatoire joué dans sa version "misère" (la condition de victoire est
  de ne pas jouer le dernier coup).
  Le jeu est somme de jeux à 1 nb dont la fonction de Grundy est la suivante :
    Grundy(1) = 0
    Grundy(n) = nb de facteurs premiers de n, comptes avec multiplicite
  On peut facilement intuiter cette fonction car il est evident que prendre
  un diviseur, c'est exactement retirer un sous-ensemble des facteurs premiers.
  La valeur de ces facteurs n'a aucune incidence ici. Dès lors, un nb ayant k
  facteurs premiers est equivalent à un tas de Nim de taille k.
  On peut aussi intuiter cette fonction par le calcul (code python ci-dessous).
  Comme le jeu est joué dans sa version misère, par analogie avec Misère Nim,
  une configuration (dans laquelle on ignore les nimbers 0 car ce sont des tas
  vides, i.e. les valeurs 1 car ce sont des valeurs finales, non jouables)
  est perdante ssi :
   - elle contient au moins un nimber > 1 (i.e. une valeur non premiere) et est
     de xor nul
   - elle ne contient que des nimbers 1 (i.e. nombres premiers) en nombre impair
  Il s'agit de compter les sous-ensembles non-vides perdants de [A,B].
  On calcule la fonction de Grundy sur [A,B] par crible.
  On compte les sous-ensembles de xor nul par prog. dyn.
  Il faut alors retirer du compte les sous-ensembles composes uniquement de nb
  premiers en nombre pair (dont l'ensemble vide) pour les remplacer par ceux
  en nb impair.
  S'il y a au moins un nb premier dans [A,B], alors il y en a autant du premier
  type que du second et le compte est déjà bon.
  Sinon, il faut retirer 1 (ensemble vide) du compte.
*/

/* # Code pour intuiter la fonction de Grundy
def mex(succ):
    i = 0
    while i in succ:
        i += 1
    return i

G = [-1]*100001
G[1] = 0
def grundy(n):
    assert(n>0)
    if G[n]>=0:
        return G[n]
    succ = {G[1]}
    D = []
    for d in range(2,int(sqrt(n))+1):
        if n%d==0:
            succ.add(grundy(d))
            succ.add(grundy(n/d))
    g = mex(succ)
    G[n] = g
    return g
*/

#include <iostream>
#include <vector>
using namespace std;

typedef long long ent;
const ent P = 1000000007;
vector<ent> L;

void sieve_list(int N) {
  vector<bool> P(N,true);
  for (int i=2; i*i<N; ++i)
    if (P[i]) {
      L.push_back(i);
      for (int k=2*i; k<N; k+=i)
	P[k] = false;
    }
}

vector<ent> grundy(ent A, ent B) {
  int N = B-A+1;
  vector<ent> G(N,0),V(N);
  for (ent i=0; i<N; ++i) V[i] = A+i;
  for (auto ip=L.begin(); ip!=L.end() && (*ip)*(*ip)<=B; ++ip) {
    ent p = *ip;
    ent x0 = max(A+p-1-((A+p-1)%p),2*p);
    for (ent x=x0; x<=B; x+=p) {
      int i = x-A;
      while (V[i]%p==0) {
	V[i] /= p;
	++G[i];
      }
    }
  }
  for (int i=0; i<N; ++i) if (V[i]>1) ++G[i];
  return G;
}

ent expmod(ent x, ent n, ent m) {
  if (!n) return 1;
  if (!(n&1)) return expmod((x*x)%m,n>>1,m);
  return (x*expmod((x*x)%m,n>>1,m))%m;
}

ent zero_xor_sub(vector<ent> &G) {
  int m = 0;
  for (auto it=G.begin(); it!=G.end(); ++it) if (m<*it) m = *it;
  int n = 1;
  while (m>=n) n <<= 1;
  vector<ent> X(n,0), Y(n,0);
  for (auto it=G.begin(); it!=G.end(); ++it) ++X[*it];
  Y[0] = 1;
  for (int x=0; x<n; ++x)
    if (X[x]>0) {
      vector<ent> Y0 = Y;
      ent p2 = expmod(2,X[x]-1,P);
      for (int y=0; y<n; ++y) {
	Y[y] = ( ((Y0[y]+Y0[y^x])%P)*p2 ) % P;
      }
    }
  return Y[0] - (ent)(X[1]==0);
}

int main() {
  sieve_list(1000000);
  int T;
  cin >> T;
  while (T--) {
    ent A,B;
    cin >> A >> B;
    vector<ent> G = grundy(A,B);
    cout << zero_xor_sub(G) << endl;
  }
  return 0;
}
