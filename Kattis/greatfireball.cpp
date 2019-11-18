/*
  O(N log N log R) approach.
  We binary search for the minimal radius.
  For each radius R, considering the center of the circle at polar-coordinates
  (R,A), we compute for each point the angular interval [Al,Ar] within which
  the center angle A must be for that point to be inside the circle.
  We sort the intervals (O(N log N) part) and compute the maximum number
  of overlapping intervals.
*/
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

const double EPS = 1e-9;
const double EPS_RAD = 5e-6;
const double RMAX = 1e6;

typedef pair<double,double> point;
#define _x_ first
#define _y_ second

int N;
vector<point> Pts;

bool angular_interval(double R, const point &P, double &al, double &ar) {
  double x = P._x_, y = P._y_;
  if (x*x+y*y > 4.*R*R) return false;
  double xm = x/2., ym = y/2.;
  double norm = sqrt(x*x+y*y);
  double vx = y/norm, vy = -x/norm;
  double h = sqrt(R*R-(xm*xm+ym*ym));
  double xl = xm+h*vx, yl = ym+h*vy;
  double xr = xm-h*vx, yr = ym-h*vy;
  al = atan2(yl,xl);
  ar = atan2(yr,xr);
  return true;
}

int best_fire(double R) {
  vector< pair<double,int> > I;
  I.reserve(2*N);
  int cnt = 0, res = 0;
  for (const point &P : Pts) {
    double al,ar;
    if (angular_interval(R,P,al,ar)) {
      if (al<ar) {
	I.push_back(make_pair(al-EPS,1));
	I.push_back(make_pair(ar+EPS,-1));
      }
      else {
	I.push_back(make_pair(al-EPS,1));
	//I.push_back(make_pair(M_PI,-1));  // useless
	//I.push_back(make_pair(-M_PI,1));
	++cnt;
	I.push_back(make_pair(ar+EPS,-1));
      }
    }
  }
  sort(I.begin(), I.end());
  for (const auto &it : I) {
    cnt += it.second;
    res = max(res, cnt);
  }
  return res;
}

int main() {
  int K;
  scanf("%d %d", &N, &K);
  Pts.reserve(N);
  for (int i=0; i<N; ++i) {
    int x,y;
    scanf("%d %d", &x, &y);
    Pts.push_back(point(x,y));
  }
  double Rmin = 0., Rmax = RMAX;
  if (best_fire(Rmax)<K) printf("-1\n");
  else {
    while (Rmax-Rmin>EPS_RAD) {
      double R = (Rmin+Rmax)/2.;
      if (best_fire(R)>=K) Rmax = R;
      else Rmin = R;
    }
    printf("%lf\n", Rmax);
  }
  return 0;
}
