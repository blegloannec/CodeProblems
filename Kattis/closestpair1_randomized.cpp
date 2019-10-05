#include <cstdio>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;

#define _x_ first
#define _y_ second
using ll = double;
typedef pair<ll,ll> point;
struct pointHash {
  size_t operator()(point const& A) const noexcept {
    return 3*((size_t)A._x_) + ((size_t)A._y_);
    //return ((size_t)A._x_) ^ (((size_t)A._y_)<<1);
    //return ((size_t)A._x_) | (((size_t)A._y_)<<32);
  }
};

/*
  Closest pair in a set of points
  Randomized algo in expected O(N)
  Not as efficient as the O(N log N) D&C in practice...
*/
int N;
vector<point> P;
unordered_map<point,int,pointHash> Box;

#define SQR(X) ((X)*(X))
ll dist(const point &A, const point &B) {
  return SQR(A._x_ - B._x_) + SQR(A._y_ - B._y_);
}

point pt_box(const point &A, ll step) {
  return make_pair(floor(A._x_/step), floor(A._y_/step));
}

ll compute_boxes(ll D, point &p, point &q) {
  ll step = (D+1)/2;
  Box.clear();
  for (int i=0; i<N; ++i) {
    point bi = pt_box(P[i],step);
    for (int x=bi._x_-2; x<=bi._x_+2; ++x)
      for (int y=bi._y_-2; y<=bi._y_+2; ++y) {
	point b(x,y);
	auto it = Box.find(b);
	if (it!=Box.end()) {
	  ll di = dist(P[i],P[it->second]);
	  if (di<D) {
	    p = P[i];
	    q = P[it->second];
	    return di;
	  }
	}
      }
    Box[bi] = i;
  }
  return D;
}

void shuffle(vector<point> &A) {
  for (int i=(int)A.size()-1; i>0; --i)
    swap(A[i],A[rand()%i]);
}

ll randomized_min_dist(point &p, point &q) {
  shuffle(P);
  ll D = dist(P[0],P[1]);
  p = P[0]; q = P[1];
  ll D0;
  do {
    D0 = D;
    D = compute_boxes(D,p,q);
  } while (D0!=D);
  return D;
}

int main() {
  srand(time(NULL));
  while (true) {
    scanf("%d", &N);
    if (N<=0) break;
    for (int i=0; i<N; ++i) {
      ll x,y;
      scanf("%lf %lf", &x, &y);
      P.push_back(point(x,y));
    }
    point p,q;
    randomized_min_dist(p,q);
    printf("%.2f %.2f %.2f %.2f\n", p._x_, p._y_, q._x_, q._y_);
    // cleaning
    P.clear();
  }
  return 0;
}
