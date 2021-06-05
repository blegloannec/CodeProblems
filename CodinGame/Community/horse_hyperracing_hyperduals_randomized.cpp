#pragma GCC optimize ("O3")
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

#define _x_ first
#define _y_ second
using ll = long long;
typedef pair<ll,ll> point;
struct pointHash {
  size_t operator()(point const& A) const noexcept {
    return 3*A._x_ + A._y_;
    //return A._x_ ^ (A._y_<<1);
    //return A._x_ | (A._y_<<32);
  }
};

// RNG
const ll RNG_A = 1103515245LL, RNG_B = 12345, RNG_MASK = (1LL<<31)-1;
ll RNG;
void rng_next() {
  RNG = (RNG_A*RNG + RNG_B) & RNG_MASK;
}

/*
  Closest pair in a set of points
  Randomized algo in expected O(N)
  Not as efficient as the O(N log N) D&C in practice...
*/
int N;
vector<point> P;
unordered_map<point,int,pointHash> Box;

ll dist(const point &A, const point &B) {
  return abs(A._x_ - B._x_) + abs(A._y_ - B._y_);
}

point pt_box(const point &A, ll step) {
  return make_pair((A._x_-(A._x_<0)*(step-1))/step,
		   (A._y_-(A._y_<0)*(step-1))/step);
}

ll compute_boxes(ll D) {
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
	  if (di<D) return di;
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

ll randomized_min_dist() {
  shuffle(P);
  ll D = dist(P[0],P[1]);
  ll D0;
  do {
    D0 = D;
    D = compute_boxes(D);
  } while (D0!=D);
  return D;
}

int main() {
  srand(time(NULL));
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
  cout << randomized_min_dist() << endl;
  return 0;
}
