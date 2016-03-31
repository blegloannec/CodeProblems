#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define MAX 301
#define INTMAX 5000000

struct edge {
  int dest,weight;
  edge(int d, int w) : dest(d), weight(w) {};
};

typedef vector<edge> liste;

int N,I,F,M;

int size;
liste t[MAX]; // Tables des listes de successeurs
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */

int dist[MAX];

liste t2[MAX]; // Tables des listes de successeurs
int pred2[MAX]; /* tableau des predecesseurs
		   A INITIALISER A -1 */

int dist2[MAX];

int filtre[MAX];
int filtre2[MAX];

void relacher(int u, int v, int w) {
  int d2 = dist[u]+w;
  if (dist[v]>d2) {
    dist[v] = d2;
    pred[v] = u;
  }
}

bool bellman_ford(liste t[], int dist[], int pred[], int start) { 
  // detecte les cycles de poids negatif
  liste::iterator it;
  for (int v=0; v<size; v++) { // initialisation
    dist[v] = INTMAX;
    pred[v] = -1;
  }
  dist[start] = 0;
  for (int j=1; j<size; j++) // relachements
    for (int u=0; u<size; u++) 
      if ((filtre[u]>=0)&&(filtre2[u]>=0)) 
	for (it=t[u].begin(); it!=t[u].end(); it++) 
	  relacher(u,it->dest,it->weight); 
  // detection des cycles negatifs, RINN
  for (int u=0; u<size; u++) 
    if ((filtre[u]>=0)&&(filtre2[u]>=0)) 
      for (it=t[u].begin(); it!=t[u].end(); it++) 
	if (dist[it->dest]>dist[u]+(it->weight)) 
	  return false;
  return true;  
}


void DFS(liste t[], int start, int pred[]) {
  pred[start] = start;
  liste::iterator it;
  for (it=t[start].begin(); it!=t[start].end(); ++it) {
    int d = it->dest;
    if (pred[d]<0) {
      pred[d] = start;
      DFS(t,d,pred);
    }
  }
}


int main() {
  int cas,a,b,s;
  bool debut = true;
  cin >> cas;

  while (cas-->0) {
    if (debut) debut = false;
    else cout << '\n';
    cin >> N >> I >> F >> M;
    size = N;
    for (int i=0; i<M; ++i) {
      cin >> a >> b >> s;
      t[a].push_back(edge(b,s));
      t2[b].push_back(edge(a,1)); // pour detecter les sommets coaccessibles
    }
    for (int i=0; i<size; ++i) {
      filtre[i] = -1;
      filtre2[i] = -1;
    }
    DFS(t,I,filtre);
    if (filtre[F]>=0) {
      DFS(t2,F,filtre2);
      if (!bellman_ford(t,dist,pred,I)) cout << "infinity\n";
      else cout << dist[F] << '\n';
    }
    else cout << "infinity\n";
    for (int i=0; i<size; ++i) {
      t[i].clear();
      t2[i].clear();
    }
  }
  return 0;
}
