#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

unsigned long long s[2];
unsigned long long xorshift128plus() {
  unsigned long long x = s[0];
  const unsigned long long y = s[1];
  x ^= x << 23;
  s[1] = x ^ y ^ (x >> 17) ^ (y >> 26);
  return s[0] = y;
}

const int MX = 1000;
int C[MX][MX];
int H[MX][MX];

struct edge {
  int u,v,w;
  edge(int u, int v, int w) : u(u),v(v),w(w) {}
  bool operator<(const edge &e2) {
    return (this->w < e2.w);
  }
};

typedef long long ent;

int n;
vector<edge> E;
vector<int> T;
bool R[MX][MX];
vector< pair<int,int> > E2;

int find(int x) {
  if (T[x]<0) return x;
  int x0 = find(T[x]);
  T[x] = x0;
  return x0;
}

void uni(int x, int y) {
  T[find(y)] = find(x);
}

void kruskal() {
  vector<int> D(n,0); // degre des sommets
  T.resize(n,-1);
  // kruskal classique pour trouver un arbre couvrant minimal
  int cpt = 0, e = 0;
  sort(E.begin(),E.end());
  //ent score = 0;
  //for (int u=0; u<n; ++u) score += H[u][0];
  while (cpt<n-1) {
    int u = E[e].u, v = E[e].v;
    if (find(u)!=find(v)) {
      uni(u,v);
      R[u][v] = true;
      R[v][u] = true;
      ++D[u]; ++D[v];
      //score += H[u][D[u]]-H[u][D[u]-1] + C[u][v] + H[v][D[v]]-H[v][D[v]-1];
      ++cpt;
    }
    ++e;
  }
  // pour chaque sommet, on ajoute des aretes de maniere a optimiser les
  // couts des hubs
  // idealement il faudrait faire plusieurs passes, integrer la
  // possibilite de supprimer des aretes, etc...
  priority_queue< pair<int,int> > Q;
  for (int u=0; u<n; ++u)
    Q.push(make_pair(H[u][D[u]],u));
  vector<bool> seen(n,false);
  while (!Q.empty()) {
    int u = Q.top().second, hu = Q.top().first;
    Q.pop();
    if (seen[u] || H[u][D[u]]!=hu) continue;
    // traitement du sommet u
    seen[u] = true;
    vector< pair<int,int> > Eu; // aretes u--v candidates a l'ajout
    for (int v=0; v<n; ++v) {
      if (v==u) continue;
      // si v a deja ete traite, on tient compte du cout de son changement
      // de hub, sinon on ne le compte pas, en prenant le pari qu'on optimisera
      // ce hub lors du traitement de v
      if (!R[u][v]) Eu.push_back(make_pair(C[u][v]+(seen[v]?H[v][D[v]+1]-H[v][D[v]]:0),v));
    }
    // calcul des ameliorations possibles du score
    sort(Eu.begin(),Eu.end());
    ent minds = 0, mind = -1;
    ent dscore = 0;
    for (int d=D[u]+1; d<n; ++d) {
      dscore += H[u][d]-H[u][d-1] + Eu[d-D[u]-1].first;
      if (dscore<minds) {
	minds = dscore;
	mind = d;
      }
    }
    if (mind>D[u]) {
      // on choisit d'ajouter des aretes pour ameliorer le score
      for (int i=0; i<mind-D[u]; ++i) {
	int v = Eu[i].second;
	++D[v];
	if (!seen[v]) Q.push(make_pair(H[v][D[v]],v));
	R[u][v] = R[v][u] = true;
      }
      D[u] = mind;
    }
  }
}

int main() {
  int TT;
  scanf("%d",&TT);
  for (int t=0; t<TT; ++t) {
    int Cmax,Hmax;
    scanf("%d %d %d",&n,&Cmax,&Hmax);
    for (int i=0; i<n; ++i) {
      C[i][i] = 0;
      scanf("%llu %llu", &s[0], &s[1]);
      for (int j=i+1; j<n; ++j)
	C[i][j] = C[j][i] = xorshift128plus() % (Cmax + 1);
    }
    for (int i=0; i<n; ++i) {
      scanf("%llu %llu",&s[0],&s[1]);
      for (int j=0; j<n; ++j)
	H[i][j] = xorshift128plus() % (Hmax + 1);
    }
    // solve here
    for (int u=0; u<n; ++u)
      for (int v=u+1; v<n; ++v)
	E.push_back(edge(u,v,C[u][v]));
    for (int u=0; u<n; ++u)
      for (int v=0; v<n; ++v)
	R[u][v] = false;
    kruskal();
    for (int u=0; u<n; ++u) {
      for (int v=0; v<n; ++v)
	printf(R[u][v]?"1":"0");
      printf("\n");
    }
    //cleaning
    E.clear();
    T.clear();
  }
  return 0;
}
