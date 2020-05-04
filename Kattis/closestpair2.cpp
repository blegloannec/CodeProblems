#include <cstdio>
#include <vector>
#include <algorithm>
#include <cfloat>
using namespace std;

#define _x_ first
#define _y_ second
using ll = double;
typedef pair<ll,ll> point;

/*
  Closest pair in a set of points
  Divide & Conquer algo in O(N log N)
  NB: there also exists a sweep line O(N log N) algo
      and an expected O(N) randomized algo
*/
int N;
vector<point> P;

#define SQR(X) ((X)*(X))
ll dist(const point &A, const point &B) {
  return SQR(A._x_ - B._x_) + SQR(A._y_ - B._y_);
}

ll min_dist(int l, int r, point &p1, point &p2) {
  if (l>=r) return DBL_MAX;
  int m = (l+r)/2;
  ll D = min_dist(l,m,p1,p2);
  point p,q;
  ll d = min_dist(m+1,r,p,q);
  if (d<D) { D = d; p1 = p; p2 = q; }
  ll mx = P[m]._x_;
  vector<point> Mid;
  for (int i=l; i<=r; ++i)
    if (SQR(abs(P[i]._x_ - mx)) < D)
      Mid.push_back(point(P[i]._y_,P[i]._x_));
  sort(Mid.begin(),Mid.end());  // sorted by y
  for (int i=0; i<(int)Mid.size(); ++i)
    // trick: checking a sliding window of size 6 is enough here
    for (int j=i+1; j<min(i+6,(int)Mid.size()); ++j) {
      d = dist(Mid[i],Mid[j]);
      if (d<D) {
	D = d;
	p1 = make_pair(Mid[i]._y_,Mid[i]._x_);
	p2 = make_pair(Mid[j]._y_,Mid[j]._x_);
      }
    }
  return D;
}

int main() {
  while (true) {
    scanf("%d", &N);
    if (N<=0) break;
    for (int i=0; i<N; ++i) {
      ll x,y;
      scanf("%lf %lf", &x, &y);
      P.push_back(point(x,y));
    }
    sort(P.begin(),P.end());  // sorted by x
    bool uniq = true;
    point p,q;
    for (int i=1; uniq && i<N; ++i)
      if (P[i-1]==P[i]) {
	p = P[i]; q = P[i]; uniq = false;
      }
    if (uniq) min_dist(0,N-1,p,q);
    printf("%.2f %.2f %.2f %.2f\n", p._x_, p._y_, q._x_ , q._y_);
    // cleaning
    P.clear();
  }
  return 0;
}
