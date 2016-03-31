/*
Local Variables: 
compile-command: "SOURCE=10983.cc;myg++"
End: 
*/

#include <iostream>
#include <list>
#include <queue>
#include <limits.h>
using namespace std;
#define MAX 30*16+11
struct edge {
  int dest,weight,p;
  edge(int d, int w, int a_p=0) : dest(d), weight(w), p(a_p) {};
};
typedef list<edge> liste;
int size=MAX;
liste t[MAX]; // Table des listes de successeurs
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */
void clear_pred(int start) { // avant un DFS
  for (int i=0; i<size; ++i) pred[i] = -1;
  pred[start] = start;
}
liste f[MAX]; // flot
liste::iterator predit[MAX]; // pointeurs sur les aretes rencontrees

bool BFS(int start, int dest) {
  // teste l'accessibilite
  if (start==dest) return true;
  queue<int> q;
  int curr;
  liste::iterator it;
  clear_pred(start);
  q.push(start);
  while (!q.empty()) {
    curr = q.front(); q.pop();
    for (it=t[curr].begin(); it!=t[curr].end(); ++it) {
      int d = it->dest;
      if (pred[d]<0) {
	q.push(d);
	pred[d] = curr;
        predit[d] = it;
	if (d==dest) return true;
      }
    }
  }
  return false;
}

void addFlow(liste t[], int src, int dst, int cap) {
  liste::iterator it = t[src].begin();
  while (it!=t[src].end()) {
    if (it->dest == dst) {
      it->weight += cap;
      if (it->weight == 0) t[src].erase(it);
      return;
    }
    ++it;
  }
  t[src].push_back(edge(dst,cap));
}

int ford_fulkerson(int source, int dest) {
  int v,cf,p,res;
  // Initialisation RINN
  for (int i=0; i<size; ++i) f[i].clear();
  // tant que l'on trouve un chemin augmentant
  while (BFS(source,dest)) { 
    // Tant que l'on touve un chemin de la source au puits 
    v = pred[dest]; // on suppose source =/= dest
    cf = predit[dest]->weight;
    while (v!=source) {
      p = pred[v];
      cf = min(cf, predit[v]->weight);
      v = p;
    }
    v = dest;
    while (v!=source) {
      p = pred[v];
      addFlow(f,p,v,cf);
      predit[v]->weight -= cf;
      if (predit[v]->weight==0) f[p].erase(predit[v]);
      addFlow(f,v,p,-cf);
      addFlow(t,v,p,cf);
      v = p;
    }
  }
  // Calcul du maxflow RINN
  res = 0;
  liste::iterator it;
  for (it=f[source].begin(); it!=f[source].end(); ++it) 
    res += it->weight;
  return res;
}

#define D 0
#define P 1

#define INF (INT_MAX >> 2)

int etat(int city, int day)
{
  return city << 4 | day;
}

int main(int argc, char *argv[])
{
  int N;
  int n, d, m;
  int u, v, c, p, e;
  int z, flot_max;
  liste gc[30*16+11];  // graphe complet
  int pm;  // cout maximum des vols examinés
  int pmin, pmax;
  bool possible;
  liste::iterator it;

  cin >> N;
  for (int i = 1; i <= N; ++i) {
    cin >> n >> d >> m;
    // construire toutes les liaisons entre jours
    for (int j = 1; j <= n; ++j)
      for (int k = 0; k < d; ++k)
	gc[etat(j, k)].push_back(edge(etat(j, k+1), INF));
    for (int j = 0; j < m; ++j) {
      cin >> u >> v >> c >> p >> e;
      u = etat(u, e);
      v = etat(v, e+1);
      gc[u].push_back(edge(v, c, p));
    }
    flot_max = 0;
    for (int j = 1; j <= n; ++j) {
      cin >> z;
      flot_max += z;
      gc[etat(0, 0)].push_back(edge(etat(j, 0), z));
    }

    possible = true;
    pmin = -1;
    pmax = 200001;
    do {
      pm = (pmin + pmax)/2;
      // copie de gc dans g en gardant seulement les vols de coût <= pm
      for (int j = 0; j < etat(n, d); ++j)
	for (it = gc[j].begin(); it != gc[j].end(); ++it)
	  if (it->p <= pm)
	    t[j].push_back(edge(it->dest, it->weight));

      if (ford_fulkerson(etat(0, 0), etat(n, d)) < flot_max) {
	if (pm == 100000) {
	  possible = false;
	  break;
	}
	pmin = pm;
      } else
	pmax = pm;

      // on vide g
      for (int j = 0; j < etat(n, d); ++j)
	t[j].clear();
    } while (pmax - pmin > 1);

    if (possible)
      cout << "Case #" << i << ": " << pmax << '\n';
    else
      cout << "Case #" << i << ": Impossible\n";

    // on vide le graphe gc
    for (int j = 0; j < etat(n, d); ++j)
      gc[j].clear();
  }

  return 0;
}
