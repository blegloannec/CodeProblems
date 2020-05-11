#include <iostream>
#include <vector>
using namespace std;

struct point {
  double x,y;
  point(double x, double y) : x(x), y(y) {}
  point operator-(const point &A) const {
    return point(x-A.x, y-A.y);
  }
  double operator*(const point &A) const {
    return x*A.y - y*A.x;
  }
  bool operator==(const point &A) const {
    return x==A.x && y==A.y;
  }
};

int sign(double x) {
  if (x==0) return 0;
  return x>0 ? 1 : -1;
}

// recycled from cleaningpipes.cpp
bool intersect(const point &A1, const point &B1, const point &A2, const point &B2) {
  point V1 = B1-A1, V2 = B2-A2;
  if (V1*V2==0) return false; // // or aligned
  // general case: testing sides
  return (sign(V1*(A2-A1))!=sign(V1*(B2-A1)) &&
	  sign(V2*(A1-A2))!=sign(V2*(B1-A2)));
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int H,W;
    cin >> H >> W;
    double X,Y,S;
    cin >> X >> Y >> S;
    point DA1(X,Y), DB1(X+S,Y+S), DA2(X,Y+S), DB2(X+S,Y);
    vector<point> P;
    for (int i=0; i<=H; ++i) {
      P.push_back(point(i,0));
      P.push_back(point(i,W));
    }
    for (int i=1; i<W; ++i) {
      P.push_back(point(0,i));
      P.push_back(point(H,i));
    }
    int N = P.size();
    vector< vector<bool> > I(N, vector<bool>(N, false));
    for (int i=0; i<N; ++i)
      for (int j=i+1; j<N; ++j)
	I[i][j] = I[j][i] = intersect(P[i],P[j],DA1,DB1) || intersect(P[i],P[j],DA2,DB2);
    int cnt = 0;
    for (int i=0; i<N; ++i)
      for (int j=i+1; j<N; ++j)
	if (!I[i][j])
	  for (int k=j+1; k<N; ++k)
	    if (!I[i][k] && !I[j][k] &&
		!(P[i].x==P[j].x && P[j].x==P[k].x) &&
		!(P[i].y==P[j].y && P[j].y==P[k].y)) {
	      ++cnt;
	    }
    cout << cnt << endl;
  }
  return 0;
}
