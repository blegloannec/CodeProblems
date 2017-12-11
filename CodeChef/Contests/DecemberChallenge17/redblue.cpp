#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long ll;
typedef long double ld;

struct point {
  ll x,y;
  int c,i;
  ld a;

  point(ll x, ll y, int c) : x(x), y(y), c(c) {}

  bool operator<(const point &B) const {
    return (this->a < B.a);
  }
};

const ld pi = M_PI;
int N,M;
vector<point> P;

ld da(ld a, ld a0) {
  a -= a0;
  if (a<0) a += 2.*pi;
  return a;
}

ll turn(point &a, point &b, point &c) {
  return (a.x-c.x)*(b.y-c.y) - (a.y-c.y)*(b.x-c.x);
}

int verif(int i, int j) {
  vector<int> C(2,0);
  for (int k=0; k<N+M; ++k) {
    if (k==i || k==j) continue;
    if (turn(P[i],P[j],P[k])>0) ++C[P[k].c];
  }
  int N0 = N - (P[i].c==0?1:0) - (P[j].c==0?1:0);
  int M0 = M - (P[i].c==1?1:0) - (P[j].c==1?1:0);
  int s = min(N0-C[0] + C[1], C[0] + M0-C[1]);
  return s;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N >> M;
    P.clear();
    for (int i=0; i<N; ++i) {
      ll x,y;
      cin >> x >> y;
      P.push_back(point(x,y,0));
    }
    for (int i=0; i<M; ++i) {
      ll x,y;
      cin >> x >> y;
      P.push_back(point(x,y,1));
    }
    if (N<=1 && M<=1) {
      cout << 0 << endl;
      continue;
    }
    vector< pair<int, pair<int,int> > > sol;
    for (int i=0; i<N+M; ++i) {
      vector<point> A;
      ll x0 = P[i].x, y0 = P[i].y;
      for (int j=0; j<N+M; ++j) {
	if (i==j) continue;
	point X = P[j];
	X.i = j;
	X.a = atan2l((ld)(X.y-y0),(ld)(X.x-x0))+pi;
	A.push_back(X);
      }
      sort(A.begin(),A.end());
      vector<int> C(2,0);
      int r = 1;
      for (int l=0; l<N+M-1; ++l) {
	if (l>0 && r!=l) --C[A[l].c];
	while (r!=l && da(A[r].a,A[l].a)<pi) {
	  ++C[A[r].c];
	  r = (r+1)%(N+M-1);
	}
	int N0 = N - (P[i].c==0?1:0) - (A[l].c==0?1:0);
	int M0 = M - (P[i].c==1?1:0) - (A[l].c==1?1:0);
	int s = min(N0-C[0] + C[1], C[0] + M0-C[1]);
	sol.push_back(make_pair(s,make_pair(i,A[l].i)));
      }
    }
    sort(sol.begin(),sol.end());
    int k = 0;
    while (verif(sol[k].second.first,sol[k].second.second)!=sol[k].first)
      ++k;
    cout << sol[k].first << endl;
  }
  return 0;
}
