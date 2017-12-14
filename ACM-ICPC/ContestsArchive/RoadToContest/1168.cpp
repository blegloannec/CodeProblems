// pb 1168 on UVa, 3982 on Archive
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

typedef unsigned int uint;
typedef vector< unordered_map<string, vector<uint> > > graph;

int L1,L2;
uint X1,X2;
graph G1,G2;

uint pack(uint u1, uint u2) {
  return u1 | (u2<<16);
}

void unpack(uint u, uint &u1, uint &u2) {
  u1 = u & ((1<<16)-1);
  u2 = u>>16;
}

int bfs() {
  queue<uint> Q;
  unordered_map<uint,int> dist;
  uint u0 = pack(0,0);
  Q.push(u0);
  dist[u0] = 0;
  while (!Q.empty()) {
    uint u = Q.front(), u1, u2;
    unpack(u,u1,u2);
    if (u1==X1 && u2==X2) return dist[u];
    Q.pop();
    for (auto is=G1[u1].begin(); is!=G1[u1].end(); ++is) {
      string s = is->first;
      if (G2[u2].find(s)!=G2[u2].end())
	for (auto iv1=G1[u1][s].begin(); iv1!=G1[u1][s].end(); ++iv1)
	  for (auto iv2=G2[u2][s].begin(); iv2!=G2[u2][s].end(); ++iv2) {
	    uint v = pack(*iv1,*iv2);
	    if (dist.find(v)==dist.end()) {
	      dist[v] = dist[u]+1;
	      Q.push(v);
	    }
	  }
    }
  }
  return -1;
}

void read_map(int &L, uint &X, graph &G) {
  int P;
  cin >> L >> X >> P;
  G.clear();
  G.resize(L);
  for (int i=0; i<P; ++i) {
    int u,v;
    string s;
    cin >> u >> s >> v;
    G[u][s].push_back(v);
  }
}

int main() {
  int cas;
  cin >> cas;
  while (cas--) {
    read_map(L1,X1,G1);
    read_map(L2,X2,G2);
    cout << bfs() << endl;
    if (cas) cout << endl;
  }
  return 0;
}
