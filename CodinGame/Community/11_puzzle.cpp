#pragma GCC optimize("O3")
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
using namespace std;

typedef long long conf;

const int H = 3;
const int W = 4;
const int S = H*W;
conf Final = 0;

conf get_cell(conf u, int b) {
  return (u>>(4*b))&15;
}

int find0(conf u) {
  int b = 0;
  while (get_cell(u,b)!=0) ++b;
  return b;
}

conf set_cell(conf u, int b, conf x) {
  return u^((get_cell(u,b)^x)<<(4*b));
}

conf swap_cells(conf u, int a, int b) {
  conf x = get_cell(u,a), y = get_cell(u,b);
  return set_cell(set_cell(u,a,y),b,x);
}

int hdist(conf u) {
  int d = 0;
  for (int i=0; i<S; ++i)
    d += abs(get_cell(u,i)/W-i/W) + abs((get_cell(u,i)%W)-(i%W));
  return d;
}

vector<conf> Astar(conf u0) {
  unordered_set<conf> Seen;
  unordered_map<conf,conf> GDist, HDist, Pred;
  GDist[u0] = 0;
  HDist[u0] = hdist(u0);
  Pred[u0] = -1;
  priority_queue< pair<int,conf> > Q;
  Q.push(make_pair(-(GDist[u0]+HDist[u0]),u0));
  while (!Q.empty()) {
    conf u = Q.top().second;
    Q.pop();
    if (u==Final) break;
    if (Seen.find(u)!=Seen.end()) continue;
    Seen.insert(u);
    int i0 = find0(u);
    int x = i0/W, y = i0%W;
    vector< pair<int,int> > V {make_pair(x-1,y),make_pair(x+1,y),make_pair(x,y-1),make_pair(x,y+1)};
    for (auto iv=V.begin(); iv!=V.end(); ++iv) {
      int vx = iv->first, vy = iv->second;
      if (0<=vx && vx<H && 0<=vy && vy<W) {
	conf v = swap_cells(u,i0,vx*W+vy);
	if (Seen.find(v)==Seen.end() && (GDist.find(v)==GDist.end() || GDist[u]+1<GDist[v])) {
	  GDist[v] = GDist[u] + 1;
	  if (HDist.find(v)==HDist.end()) HDist[v] = hdist(v);
	  Pred[v] = u;
	  Q.push(make_pair(-(GDist[v]+HDist[v]),v));
	}
      }
    }
  }
  vector<conf> Path;
  conf u = Final;
  while (u>=0) {
    Path.push_back(u);
    u = Pred[u];
  }
  reverse(Path.begin(),Path.end());
  return Path;
}

int main() {
  for (conf i=0; i<S; ++i) Final |= i<<(4*i);
  conf u0 = 0;
  for (int i=0; i<H; ++i)
    for (int j=0; j<W; ++j) {
      conf c;
      cin >> c;
      u0 = set_cell(u0,i*W+j,c);
    }
  vector<conf> Path = Astar(u0);
  int k = 1;
  while (k<(int)Path.size()) {
    conf v = Path[k];
    int i0 = find0(v);
    cout << i0/W << ' ' << i0%W << endl;
    ++k;
  }
  return 0;
}
