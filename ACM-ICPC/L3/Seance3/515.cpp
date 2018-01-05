#include <iostream>
#include <list>
using namespace std;

#define MAX 1002
#define INTMAX 500000
#define S 1

struct edge {
  int e,w;
  edge(int ext, int weight) : e(ext), w(weight) {};
};

int n;
list<edge> adj[MAX];
int pi[MAX];
int d[MAX];

void clearg() {
  for (int i=1; i<=n; i++) adj[i].clear();
}

void init() {
  for (int v=1; v<=n; v++) {
    d[v] = INTMAX;
    pi[v] = 0;
  }
  d[S] = 0;
}

void relacher(int u, int v, int w) {
  int d2 = d[u]+w;
  if (d[v]>d2) {
    d[v] = d2;
    pi[v] = u;
  }
}

bool bellman_ford() {
  list<edge>::iterator it;
  init();
  for (int j=1; j<n; j++)
    for (int u=1; u<=n; u++) 
      for (it=adj[u].begin(); it!=adj[u].end(); it++) 
	relacher(u,it->e,it->w);
  for (int u=1; u<=n; u++) 
    for (it=adj[u].begin(); it!=adj[u].end(); it++) 
      if (d[it->e]>d[u]+(it->w)) {
	return false;
      }
  return true;  
}

/*
void affich() {
  for (int i=1; i<=n; i++) {
    for (list<edge>::iterator it=adj[i].begin(); it!=adj[i].end(); it++) 
      cout << '(' << i << ' ' << it->e << ' ' << it->w << ") ";
    cout << endl;
  }
}
*/

int main() {
  int m,e1,e2,p;
  char* op = (char*) malloc(3*sizeof(char));
  while (cin >> n >> m) {
    ++n;
    clearg();
    while (m-->0) {
      cin >> e1 >> e2 >> op >> p;
      e2 += e1+1;
      if (!strcmp(op,"lt")) adj[e1].push_front(edge(e2,p-1));
      else adj[e2].push_front(edge(e1,-p-1));
    }
    if (!bellman_ford()) cout << "successful conspiracy" << endl;
    else cout << "lamentable kingdom" << endl;
  }
  return 0;
}
