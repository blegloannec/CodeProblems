// Archive 3850 -  Here We Go(relians) Again
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef vector< pair<int,int> > edges;
const int R = 2520;
int h,w;
vector<edges> G;

int V(int i, int j) {
  return i*w+j;
}

int dijkstra(int u0, int ud) {
  vector<int> D(h*w,-1);
  priority_queue< pair<int,int> > Q;
  D[u0] = 0;
  Q.push(make_pair(0,u0));
  while (!Q.empty()) {
    int d = -Q.top().first, u = Q.top().second;
    Q.pop();
    if (u==ud) break;
    if (d>D[u]) continue;
    for (edges::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv) {
      int v = iv->first, s = iv->second;
      if (D[v]<0 || d+s<D[v]) {
	D[v] = d+s;
	Q.push(make_pair(-D[v],v));
      }
    }
  }
  return D[ud];
}

int main() {
  while (cin >> h >> w) {
    if (h==0) break;
    ++h; ++w;
    G.resize(h*w);
    for (int l=0; l<2*h-1; ++l) {
      int i = l/2;
      if (l%2==0)
	for (int j=0; j<w-1; ++j) {
	  int s; char d;
	  cin >> s >> d;
	  if (s>0) {
	    if (d!='<') G[V(i,j)].push_back(make_pair(V(i,j+1),R/s));
	    if (d!='>') G[V(i,j+1)].push_back(make_pair(V(i,j),R/s));
	  }
	}
      else
	for (int j=0; j<w; ++j) {
	  int s; char d;
	  cin >> s >> d;
	  if (s>0) {
	    if (d!='^') G[V(i,j)].push_back(make_pair(V(i+1,j),R/s));
	    if (d!='v') G[V(i+1,j)].push_back(make_pair(V(i,j),R/s));
	  }
	}
    }
    int d = dijkstra(0,h*w-1);
    if (d<0) cout << "Holiday" << endl;
    else cout << d << " blips" << endl;
    // cleaning
    G.clear();
  }
  return 0;
}
