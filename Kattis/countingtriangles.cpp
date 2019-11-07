#include <iostream>
#include <vector>
using namespace std;

struct point {
  double x,y;
  point(double x, double y) : x(x), y(y) {}
  point operator-(const point &A) const {
    return point(-(x-A.x), -(y-A.y));
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
  //if (A1==A2 || A1==B2 || B1==A2 || B2==A2) return true;
  point V1 = B1-A1, V2 = B2-A2;
  if (V1*V2==0) return false; // // or aligned
  // general case: testing sides
  return (sign(V1*(A2-A1))!=sign(V1*(B2-A1)) &&
	  sign(V2*(A1-A2))!=sign(V2*(B1-A2)));
}

int main() {
  while (true) {
    int N;
    cin >> N;
    if (N<=0) break;
    vector<point> A,B;
    for (int i=0; i<N; ++i) {
      double x1,y1,x2,y2;
      cin >> x1 >> y1 >> x2 >> y2;
      A.push_back(point(x1,y1));
      B.push_back(point(x2,y2));
    }
    int cnt = 0;
    vector< vector<bool> > I(N, vector<bool>(N));
    for (int i=0; i<N; ++i)
      for (int j=i+1; j<N; ++j)
	I[i][j] = intersect(A[i],B[i],A[j],B[j]);
    for (int i=0; i<N; ++i)
      for (int j=i+1; j<N; ++j)
	if (I[i][j])
	  for (int k=j+1; k<N; ++k)
	    if (I[i][k] && I[j][k])
	      ++cnt;
    cout << cnt << "\n";
  }
  return 0;
}
