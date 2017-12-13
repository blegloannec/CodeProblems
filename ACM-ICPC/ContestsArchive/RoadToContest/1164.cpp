// pb 1164 on UVa, 3648 on Archive
#include <iostream>
#include <vector>
#include <queue>
#include <map>
using namespace std;

typedef tuple<int,int,int> triple;

int W,H,x0,y0,x1,y1;
vector< vector<char> > G;
vector<int> L(26);

int lvl(char c) {
  return L[c-'A'];
}

int bfs() {
  queue<triple> Q;
  triple u0(x0,y0,(G[x0][y0]=='o' ? -1 : lvl(G[x0][y0])));
  map<triple,int> dist;
  dist[u0] = 0;
  Q.push(u0);
  while (!Q.empty()) {
    triple u = Q.front();
    int x,y,l;
    tie(x,y,l) = u;
    if (x==x1 && y==y1) return dist[u];
    Q.pop();
    vector< pair<int,int> > V {make_pair(x-1,y),make_pair(x+1,y),make_pair(x,y-1),make_pair(x,y+1)};
    for (auto iv=V.begin(); iv!=V.end(); ++iv) {
      int vx = iv->first, vy = iv->second;
      if (0<=vx && vx<H && 0<=vy && vy<W && G[vx][vy]!='x' && (G[vx][vy]=='o' || l<lvl(G[vx][vy]))) {
	triple v(vx,vy,(G[vx][vy]=='o' ? l : lvl(G[vx][vy])));
	if (dist.find(v)==dist.end()) {
	  dist[v] = dist[u]+1;
	  Q.push(v);
	}
      }
    }
  }
  return -1;
}

int main() {
  char c;
  while (cin >> c) {
    L[c-'A'] = 0;
    for (int i=1; i<26; ++i) {
      cin >> c;
      L[c-'A'] = i;
    }
    cin >> W >> H;
    G.resize(H);
    for (int i=0; i<H; ++i) {
      G[i].resize(W);
      for (int j=0; j<W; ++j)
	cin >> G[i][j];
    }
    cin >> y0 >> x0 >> y1 >> x1;
    int d = bfs();
    if (d<0) cout << "IMPOSSIBLE" << endl;
    else cout << d << endl;
    // cleaning
    G.clear();
  }
  return 0;
}
