#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int n,m,k;
vector< vector<char> > G;
vector< vector<int> > dist;

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
  printf("%d\n",bfs(x1-1,y1-1,x2-1,y2-1));
  return 0;
}
