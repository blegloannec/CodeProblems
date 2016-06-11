#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;

typedef pair<int,int> couple;
struct arete {
  int k,u,v;
  arete(int a, int b, int c) : k(a), u(b), v(c) {}
};
bool comp_arete(arete a, arete b) { return (a.k < b.k); }
typedef set<int> couleurs;
typedef set<couple> requetes;
struct comp {
  bool operator()(couple &v1, couple &v2) {
    return (v1.first > v2.first);
  }
};
typedef priority_queue<couple,vector<couple>,comp> prio;

int n,m,q;
vector<int> t,T;
vector<couleurs> S;
vector<requetes> R0;
vector<prio> R1;
vector<int> Sol;

int find(int x) {
  if (T[x]<0) return x;
  int x0 = find(T[x]);
  T[x] = x0;
  return x0;
}

void uni(int x, int y, int w) {
  int x0 = find(x);
  int y0 = find(y);
  T[y0] = x0;

  // transfert des couleurs
  if (S[x0].size()<S[y0].size()) swap(S[x0],S[y0]);
  while (!S[y0].empty()) {
    S[x0].insert(*S[y0].begin());
    S[y0].erase(S[y0].begin());
  }

  // transfert des requetes partielles
  if (R0[x0].size()<R0[y0].size()) swap(R0[x0],R0[y0]);
  while (!R0[y0].empty()) {
    requetes::iterator it = R0[y0].begin();
    if (R0[x0].find(*it) != R0[x0].end()) {
      // villes reunies, resolution ou mise en attente
      R0[x0].erase(*it);
      if (it->first <= (int)S[x0].size()) Sol[it->second] = w;
      else R1[x0].push(*it);
    }
    // requetes restant partielles
    else R0[x0].insert(*it);
    R0[y0].erase(it);
  }

  // transfert des requetes en atteinte
  if (R1[x0].size()<R1[y0].size()) swap(R1[x0],R1[y0]);
  while (!R1[y0].empty()) {
    R1[x0].push(R1[y0].top());
    R1[y0].pop();
  }
  // traitement des requetes en attente
  // on depile les requetes dont le nb de couleurs est atteint
  while (!R1[x0].empty() && R1[x0].top().first <= (int)S[x0].size()) {
    Sol[R1[x0].top().second] = w;
    R1[x0].pop();
  }
}

void tarjan(vector<arete> E) {
  for (vector<arete>::iterator it=E.begin(); it!=E.end(); ++it)
    if (find(it->u)!=find(it->v))
      uni(it->u, it->v, it->k);
}

int main() {
  cin >> n >> m >> q;
  
  t = vector<int>(n);
  for (int i=0; i<n; ++i) cin >> t[i];
  
  vector<arete> E = vector<arete>();
  for (int i=0; i<m; ++i) {
    int x,y,k;
    cin >> x >> y >> k;
    E.push_back(arete(k,x-1,y-1));
  }
  sort(E.begin(),E.end(),comp_arete);

  // tableau des composantes (pour union-find)
  T = vector<int>(n,-1);
  // S[u] contiendra les couleurs des villes de la composante
  // connexe representee par u
  S = vector<couleurs>(n);
  for (int i=0; i<n; ++i) S[i].insert(t[i]);
  // R0[u] contiendra les requetes concernant une ville de la
  // composante representee par u et une ville non encore
  // dans la composante
  R0 = vector<requetes>(n);
  // R1[u] contiendra les requetes concernant 2 villes de la
  // composante representee par u et dont le nombre de couleurs
  // n'est pas encore atteint
  R1 = vector<prio>(n);
  // Solutions aux requetes
  Sol = vector<int>(q,-1);

  for (int i=0; i<q; ++i) {
    int x,y,k;
    cin >> x >> y >> k;
    if (x==y) {
      if (k==0) Sol[i] = 0;
      else R1[x-1].push(couple(k,i));
    }
    else {
      R0[x-1].insert(couple(k,i));
      R0[y-1].insert(couple(k,i));
    }
  }
  
  tarjan(E);
  for (int i=0; i<q; ++i) cout << Sol[i] << endl;
  return 0;
}
