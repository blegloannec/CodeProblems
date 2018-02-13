#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

// n the nb of points, m the nb of boxes
// O(n + m) approach here using DP
// a more naive O(n + m^2) approach would be good enough as m << n

typedef long long ent;
typedef pair<double,double> point;
typedef vector<point> points;

const int M = 10;
int n;
points B[M][M];
ent LinC[M][M],RecC[M][M];
double BS[M][M],LinS[M][M],RecS[M][M];

void init() {
  for (int i=0; i<M; ++i)
    for (int j=0; j<M; ++j) {
      B[i][j].clear();
      BS[i][j] = 0.;
    }
}

int main() {
  while (scanf("%d",&n)==1) {
    init();
    for (int i=0; i<n; ++i) {
      double x,y;
      scanf("%lf %lf",&x,&y);
      int bx = (int)x, by = (int)y;
      B[bx][by].push_back(make_pair(x,y));
      BS[bx][by] += x-bx + y-by;
    }
    for (int i=0; i<M; ++i)
      for (int j=0; j<M; ++j) {
	LinC[i][j] = B[i][j].size();
	LinS[i][j] = 2.*B[i][j].size() - BS[i][j];
	if (j>0) {
	  LinC[i][j] += LinC[i][j-1];
	  LinS[i][j] += LinS[i][j-1] + LinC[i][j-1];
	}
      }
    double d = 0.;
    ent c = 0;
    for (int i=0; i<M; ++i)
      for (int j=0; j<M; ++j) {
	RecC[i][j] = LinC[i][j] + (i ? RecC[i-1][j] : 0.);
	RecS[i][j] = LinS[i][j] + (i ? RecS[i-1][j]+RecC[i-1][j] : 0.);
	if (i&&j) {
	  d += RecS[i-1][j-1]*B[i][j].size() + BS[i][j]*RecC[i-1][j-1];
	  c += B[i][j].size()*RecC[i-1][j-1];
	}
      }
    double res = round(1e8*d/c)/1e8;
    printf("%.8lf\n",res);
  }
  return 0;
}
