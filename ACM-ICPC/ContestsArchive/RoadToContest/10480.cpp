#include <iostream>
#include <list>
#include <queue>
using namespace std;

#define MAX 51

struct edge {
  int dest,weight;
  edge(int d, int w) : dest(d), weight(w) {};
};

typedef list<edge> liste;

int size;
liste t[MAX]; // Table des listes de successeurs
liste t0[MAX]; // Table des listes de successeurs
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */

void clear_pred(int start) {
  for (int i=0; i<size; ++i) pred[i]=-1;
  pred[start] = start;
}


liste f[MAX]; // flot
liste::iterator predit[MAX]; // pointeurs sur les aretes rencontrees

bool BFS(int start, int dest) {
  if (start==dest) return true; // RINN
  queue<int> q;
  int curr;
  liste::iterator it;
  q.push(start);
  clear_pred(start);
  while (!q.empty()) {
    curr = q.front(); q.pop();
    for (it=t[curr].begin(); it!=t[curr].end(); ++it) {
      int d = it->dest;
      if (pred[d]<0) {
	q.push(d);
	pred[d] = curr;  
	predit[d] = it;
	if (d==dest) return true; // SINN
      }
    }
  }
  return false; // RINN
}


/* Ajouter ce code dans le BFS :
   Juste apres :
   pred[d] = curr;
   Ajouter :
   predit[d] = it; */
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

void DFS(int start) {
  liste::iterator it;
  for (it=t[start].begin(); it!=t[start].end(); ++it) {
    int d = it->dest;
    if (pred[d]<0) {
      pred[d] = start;
      DFS(d);
    }
  }
}

void cut_edges(int source) {
  liste::iterator it;
  clear_pred(source);
  DFS(source);
  for (int i=0; i<size; ++i)
    if (pred[i]>=0) 
      for (it=t0[i].begin(); it!=t0[i].end(); ++it)
	if (pred[it->dest]<0) 
	  cout << i+1 << ' ' << it->dest+1 << '\n';
}

int main() {
  int m,a,b,c;
  while (cin >> size >> m) {
    if (size==0) return 0;
    for (int i=0; i<m; ++i) {
      cin >> a >> b >> c;
      --a;
      --b;
      t[a].push_back(edge(b,c));
      t[b].push_back(edge(a,c));
      t0[a].push_back(edge(b,c));
      t0[b].push_back(edge(a,c));
    }
    ford_fulkerson(0,1);
    cut_edges(0);
    // for (int i=0; i<size; ++i) 
      //cout << pred[i] << endl;
    for (int i=0; i<size; ++i) {
      t[i].clear();
      t0[i].clear();
    }
    cout << '\n';
  }
  return 0;
}
