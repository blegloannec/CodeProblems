#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

#define _x_ first
#define _y_ second
using ll = long long;
typedef pair<ll,ll> point;

// RNG
const ll RNG_A = 1103515245LL, RNG_B = 12345, RNG_MASK = (1LL<<31)-1;
ll RNG;
void rng_next() {
  RNG = (RNG_A*RNG + RNG_B) & RNG_MASK;
}

/*
  Closest pair in a set of points
  Divide & Conquer algo in O(N log N)
  NB: there also exists a sweep line O(N log N) algo
      and an expected O(N) randomized algo
*/
int N;
vector<point> P;

ll dist(point &A, point &B) {
  return abs(A._x_ - B._x_) + abs(A._y_ - B._y_);
}

ll min_dist(int l, int r) {
  if (l>=r) return LONG_MAX;
  int m = (l+r)/2;
  ll D = min(min_dist(l,m),min_dist(m+1,r));
  ll mx = P[m]._x_;
  vector<point> Mid;
  for (int i=l; i<=r; ++i)
    if (abs(P[i]._x_ - mx) < D)
      Mid.push_back(point(P[i]._y_,P[i]._x_));
  sort(Mid.begin(),Mid.end());  // sorted by y
  for (int i=0; i<(int)Mid.size(); ++i)
    // trick: checking a sliding window of size 6 is enough here
    for (int j=i+1; j<min(i+6,(int)Mid.size()); ++j)
      D = min(D,dist(Mid[i],Mid[j]));
  return D;
}

int main() {
  int M;
  cin >> N >> M >> RNG;
  for (int i=0; i<N; ++i) {
    ll x,y;
    cin >> x >> y;
    P.push_back(point(x,y));
  }
  for (int i=0; i<M; ++i) {
    ll x = RNG; rng_next();
    ll y = RNG; rng_next();
    P.push_back(point(x,y));
  }
  N += M;
  sort(P.begin(),P.end());  // sorted by x
  cout << min_dist(0,N-1) << endl;
  return 0;
}
