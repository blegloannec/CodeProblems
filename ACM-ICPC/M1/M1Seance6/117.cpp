#include <iostream>
#include <vector>
#include <queue>
#define MAX 26
using namespace std;

int degre[26];

struct edge {
  int dest,weight;
  edge(int d, int w) : dest(d), weight(w) {};
};

typedef vector<edge> liste;
int size;
liste t[MAX]; // Table des listes de successeurs
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */
void clear_pred(int start) { // avant un DFS
  for (int i=0; i<size; ++i) pred[i] = -1;
  pred[start] = start;
}

struct vert {
  int num,dist;
  vert(int n, int d) : num(n),dist(d) {};
};

struct comp {
  bool operator()(vert &v1, vert &v2) {
    return (v1.dist > v2.dist);
  };
};

int dist[MAX];
bool visited[MAX];

void relacher(int u, int v, int w) {
  int d2 = dist[u]+w;
  if ((dist[v]<0)||(dist[v]>d2)) {
    dist[v] = d2;
    pred[v] = u;
  }
}

bool dijkstra(int start, int dest) { // teste si l'on atteint dest
  int u;
  liste::iterator it; // RINN
  priority_queue<vert,vector<vert>,comp> q;
  // initialisation
  for (int i=0; i<size; i++) {
    dist[i] = -1;
    pred[i] = -1;
    visited[i] = false;
  }
  dist[start] = 0;
  q.push(vert(start,0));
  while (!q.empty()) { // BFS
    u = q.top().num;
    if (u==dest) return true; // RINN
    q.pop();
    if (!visited[u]) {
      for (it=t[u].begin(); it!=t[u].end(); ++it) {
	int v = it->dest;
	relacher(u,v,it->weight);
	if (!visited[v]) q.push(vert(v,dist[v]));
      }
      visited[u] = true;
    }
  }
  return false; // RINN
}


int main() {
  string s;
  int a,b,c,total,bonus;
  int impairs[2];
  size = 26;
  total = 0;
  while (cin >> s) {
    if (s=="deadend") {
      c = 0;
      for (int i=0; i<26; ++i) {
        if ((int)t[i].size() % 2 == 1) {
          impairs[c++] = i;
        }
        if (c == 2) break;
      }
      bonus = 0;
      if (c>0) {
        dijkstra(impairs[0],impairs[1]);
        bonus = dist[impairs[1]];
      }
      cout << total+bonus << '\n';
      for (int i=0; i<26; ++i) {
        t[i].clear();
      }
      total = 0;
      continue;
    }
    a = s[0]-'a';
    b = s[s.size()-1]-'a';
    degre[a] += 1;
    degre[b] += 1;
    total += s.size();
    t[a].push_back(edge(b,s.size()));
    t[b].push_back(edge(a,s.size()));
  }
  
  return 0;
}
