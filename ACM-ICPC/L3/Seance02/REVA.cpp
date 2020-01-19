// Re-Etiqueter Vers l'Avant pour Sabotage

#include <iostream>
#include <list>
using namespace std;

#define MAX 51
#define SOURCE 1
#define SINK 2
#define INTMAX 50000000

int c[MAX][MAX]; // capacites
int f[MAX][MAX]; // preflot
int h[MAX];      // hauteurs
int e[MAX];      // excedents
int seen[MAX];   // derniers sommets visites
list<int> liste; // liste
int n;           // nb de sommets

void push(int u, int v) {
  int send = min(e[u], c[u][v]-f[u][v]);
  f[u][v] += send;
  f[v][u] -= send;
  e[u] -= send;
  e[v] += send;
}

void relabel(int u) {
  int min_height = h[u];
  for (int v=1; v<=n; v++) {
    if (c[u][v]-f[u][v]>0) {
      min_height = min(min_height, h[v]);
      h[u] = min_height+1;
    }
  }
}

void discharge(int u) {
  while (e[u] > 0) {
    if (seen[u] < n) {
      for (int v=1; v<=n; v++) {
	if ((c[u][v] - f[u][v] > 0) && (h[u] > h[v])) push(u,v);
	else ++(seen[u]);
      }
    }
    else {
      relabel(u);
      seen[u] = 0;
    }
  }
}

void clear() {
  for (int i=1; i<=n; i++)
    for (int j=1; j<=n; j++) 
      c[i][j] = 0;
}

void init() {
  liste.clear();
  for (int i=1; i<=n; i++) {
    if ((i!=SOURCE) && (i!=SINK)) liste.push_back(i);
    h[i] = 0;
    e[i] = 0;
    seen[i] = 0;
    for (int j=0; j<=n; j++) {
      f[i][j] = 0;
    }
  }
  h[SOURCE] = n;
  e[SOURCE] = INTMAX;
  for (int v=1; v<=n; v++) push(SOURCE,v);
}

void print(int t[MAX][MAX]) {
  for (int i=1; i<=n; i++) {
    for (int j=1; j<=n; j++)
      cout << t[i][j] << '\t';
    cout << endl;
  }
  cout << endl;
}
  
int main() {
  int m;
  while (cin >> n >> m) {
    clear();
    for (int k=0; k<m; k++) {
      int u,v,w;
      cin >> u >> v >> w;
      c[u][v] = w;
      c[u][v] = w;
    }
    //print(c);
    init();
    list<int>::iterator p = liste.begin();
    while (p!=liste.end()) {
      int u = *p;
      int old_height = h[u];
      discharge(u);
      if (h[u] > old_height) {
	liste.erase(p);
	liste.push_front(u);
	p = liste.begin();
      }
      ++p;
    } 
    print(f);
  }
  return 0;
}
