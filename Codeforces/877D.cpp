#include <cstdio>
#include <vector>
#include <queue>
#include <set>
using namespace std;

int n,m,k;
vector< vector<char> > G;
vector< vector<int> > dist;

// BFS optimise en O(nmk), passe tout juste
int bfs(int x0, int y0, int xd, int yd) {
  queue< pair<int,int> > Q;
  Q.push(make_pair(x0,y0));
  dist[x0][y0] = 0;
  while (!Q.empty()) {
    int x = Q.front().first, y = Q.front().second;
    Q.pop();
    if (x==xd && y==yd) return dist[xd][yd];
    for (int l=1; l<=k; ++l) {
      int xv = x-l, yv = y;
      if (0<=xv && xv<n && 0<=yv && yv<m && G[xv][yv]=='.') {
	if (dist[xv][yv]<0) {
	  dist[xv][yv] = dist[x][y]+1;
	  if (xv==xd && yv==yd) return dist[xd][yd];
	  Q.push(make_pair(xv,yv));
	}
      }
      else break;
    }
    for (int l=1; l<=k; ++l) {
      int xv = x+l, yv = y;
      if (0<=xv && xv<n && 0<=yv && yv<m && G[xv][yv]=='.') {
	if (dist[xv][yv]<0) {
	  dist[xv][yv] = dist[x][y]+1;
	  if (xv==xd && yv==yd) return dist[xd][yd];
	  Q.push(make_pair(xv,yv));
	}
      }
      else break;
    }
    for (int l=1; l<=k; ++l) {
      int xv = x, yv = y-l;
      if (0<=xv && xv<n && 0<=yv && yv<m && G[xv][yv]=='.') {
	if (dist[xv][yv]<0) {
	  dist[xv][yv] = dist[x][y]+1;
	  if (xv==xd && yv==yd) return dist[xd][yd];
	  Q.push(make_pair(xv,yv));
	}
      }
      else break;
    }
    for (int l=1; l<=k; ++l) {
      int xv = x, yv = y+l;
      if (0<=xv && xv<n && 0<=yv && yv<m && G[xv][yv]=='.') {
	if (dist[xv][yv]<0) {
	  dist[xv][yv] = dist[x][y]+1;
	  if (xv==xd && yv==yd) return dist[xd][yd];
	  Q.push(make_pair(xv,yv));
	}
      }
      else break;
    }
  }
  return -1;
}


// BFS en O(nm log nm) en retirant les sommets deja visites
// grace a une representation du graphe en lignes/colonnes
// avec des BST
vector< set<int> > L,C;
queue< pair<int,int> > Q;

inline void push_point(int x, int y, int x0, int y0) {
  dist[x][y] = dist[x0][y0]+1;
  Q.push(make_pair(x,y));
  L[x].erase(y);
  C[y].erase(x);
}

int bfs_sets(int x0, int y0, int xd, int yd) {
  L.resize(n);
  for (int i=0; i<n; ++i)
    for (int j=0; j<m; ++j) L[i].insert(j);
  C.resize(m);
  for (int j=0; j<m; ++j)
    for (int i=0; i<n; ++i) C[j].insert(i);
  push_point(x0,y0,x0,y0);
  while (!Q.empty()) {
    int x = Q.front().first, y = Q.front().second;
    Q.pop();
    if (x==xd && y==yd) break;
    auto it = L[x].lower_bound(y);
    while (it!=L[x].end() && *it-y<=k && G[x][*it]=='.') {
      push_point(x,*it,x,y);
      it = L[x].lower_bound(y);
    }
    it = L[x].lower_bound(y);
    while (it!=L[x].begin()) {
      --it;
      if (!(y-*it<=k && G[x][*it]=='.')) break;
      push_point(x,*it,x,y);
      it = L[x].lower_bound(y);
    }
    it = C[y].lower_bound(x);
    while (it!=C[y].end() && *it-x<=k && G[*it][y]=='.') {
      push_point(*it,y,x,y);
      it = C[y].lower_bound(x);
    }
    it = C[y].lower_bound(x);
    while (it!=C[y].begin()) {
      --it;
      if (!(x-*it<=k && G[*it][y]=='.')) break;
      push_point(*it,y,x,y);
      it = C[y].lower_bound(x);
    }
  }
  return dist[xd][yd];
}

int main() {
  scanf("%d %d %d",&n,&m,&k);
  G.resize(n);
  dist.resize(n);
  for (int i=0; i<n; ++i) {
    G[i].resize(m);
    dist[i].resize(m,-1);
    for (int j=0; j<m; ++j) scanf(" %c",&G[i][j]);
  }
  int x1,y1,x2,y2;
  scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
  printf("%d\n",bfs_sets(x1-1,y1-1,x2-1,y2-1));
  return 0;
}
