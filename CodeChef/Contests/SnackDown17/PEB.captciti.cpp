#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

/*
  Prog. dyn. sur un arbre.
  On enracine l'arbre de maniere arbitraire et l'on pose
  dp0[u] = cout minimal de la conquete du sous-arbre enracine en u
           en considerant que le pere de u sera conquis apres
  dp1[u] = idem en considerant le pere de u deja conquis
  Par definition, dp0[u] >= dp1[u].
*/

typedef long long ll;
int N;
vector< vector<int> > G;
vector<ll> P,C,dp0,dp1;

void dfs(int u, int u0=-1) {
  ll s0 = 0, s1 = 0;
  vector< pair<ll,int> > S0;
  for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0) {
      dfs(*iv,u);
      s1 += dp1[*iv];
      S0.push_back(make_pair(dp0[*iv]-dp1[*iv],*iv));
    }
  // cout de l'achat de u
  ll a = P[u]+s1;
  // cout de la contamination de u
  // on doit payer C[u], ou C[u]-1 si le pere est deja contamine,
  // valeurs dp0 des fils et le reste en dp1
  // les fils sont donc tries par ordre de dp0-dp1 (les plus profitables
  // a payer en dp0 sont ceux dont l'ecart avec dp1 est le plus faible)
  sort(S0.begin(),S0.end());
  for (int i=0; i<(int)S0.size(); ++i)
    s0 += i<C[u]-1 ? dp0[S0[i].second] : dp1[S0[i].second];
  dp1[u] = min(a,s0);
  if (C[u]<=(int)S0.size()) dp0[u] = min(a,s0+S0[C[u]-1].first);
  else dp0[u] = a;
}

int main() {
  int T,u,v;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    scanf("%d",&N);
    G.resize(N);
    for (int i=0; i<N-1; ++i) {
      scanf("%d %d",&u,&v); --u; --v;
      G[u].push_back(v);
      G[v].push_back(u);
    }
    P.resize(N);
    C.resize(N);
    for (int i=0; i<N; ++i) scanf("%lld",&P[i]);
    for (int i=0; i<N; ++i) scanf("%lld",&C[i]);
    dp0.resize(N);
    dp1.resize(N);
    dfs(0);
    printf("%lld\n",dp0[0]);
    // cleaning
    G.clear();
  }
  return 0;
}
