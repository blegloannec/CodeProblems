#include <iostream>
#include <list>
using namespace std;

#define MAX 1001
#define INTMAX 50000000
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

void relacher(int u, int v,int w) {
  int d2 = d[u]+w;
  if (d[v]>d2) {
    d[v] = d2;
    pi[v] = u;
  }
}

bool bellman_ford() {
  list<edge>::iterator it;
  init();
  //for (int j=1; j<n; j++)
  for (int u=1; u<=n; u++) 
    for (it=adj[u].begin(); it!=adj[u].end(); it++) 
      relacher(u,it->e,it->w);
  for (int u=1; u<=n; u++) 
    for (it=adj[u].begin(); it!=adj[u].end(); it++) 
      if (d[it->e]>d[u]+(it->w)) return false;
  return true;  
}

int main() {
  int c,m;
  cin >> c;
  while (c-->0) {
    clearg();
    cin >> n >> m;
    while (m-->0) {
      int e1,e2,p;
      cin >> e1 >> e2 >> p;
      adj[e1+1].push_front(edge(e2+1,p));
    }
    if (!bellman_ford()) cout << "possible" << endl;
    else cout << "not possible" << endl;
  }
  return 0;
}
