#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int,ll> couple;

int n;
vector<int> C;
vector< vector<couple> > G;

ll sum(int u, int u0, ll &nr, ll &rr, ll &nb, ll &rb) {
  ll res = 0; // somme chemins rouge->noir dans le sous-arbre de u
  nr = 0;     // nb sommets rouges dans le sous-arbre de u
  rr = 0;     // somme chemins u->rouge dans le sous-arbre de u
  nb = 0; rb = 0; // idem noirs
  int V = G[u].size();
  // premiere passe ou l'on calcule les quatre valeurs precedentes
  // et on memorise celles associees a chacun des fils
  vector<ll> NR(V),NB(V),RR(V),RB(V);
  for (int i=0; i<V; ++i) {
    int v = G[u][i].first;
    ll w = G[u][i].second;
    if (v!=u0) {
      // on ajoute le compte des chemins internes au sous-arbre de v :
      res += sum(v,u,NR[i],RR[i],NB[i],RB[i]);
      nr += NR[i]; nb += NB[i];
      // chemins u->rouge/noir, ajout de l'arete u->v :
      RR[i] += w*NR[i]; rr += RR[i];
      RB[i] += w*NB[i]; rb += RB[i];
      // si u rouge/noir on ajoute au resultat les chemins u->v->noir/rouge
      res += C[u]==0 ? RB[i] : RR[i];
    }
  }
  // seconde passe ou l'on calcule les chemins rouge -> v -> u -> v' -> noir, v =/= v'
  for (int i=0; i<(int)G[u].size(); ++i)
    if (G[u][i].first!=u0)
      //   (nb de noirs hors du sous-arbre de v)  * (somme des rouge->u du sous-arbre de v)
      // + (nb de rouges dans le sous-arbre de v) * (somme des u->noir hors du sous-arbre de v)
      res += (nb-NB[i])*RR[i] + NR[i]*(rb-RB[i]);
  // on compte u :
  if (C[u]==0) ++nr;
  else ++nb;
  return res;
}

int main() {
  cin >> n;
  C.resize(n);
  for (int i=0; i<n; ++i) cin >> C[i];
  G.resize(n);
  for (int i=0; i<n-1; ++i) {
    int u,v; ll w;
    cin >> u >> v >> w; --u; --v;
    G[u].push_back(couple(v,w));
    G[v].push_back(couple(u,w));
  }
  ll nr,rr,nb,rb;
  cout << sum(0,-1,nr,rr,nb,rb) << endl;
  return 0;
}
