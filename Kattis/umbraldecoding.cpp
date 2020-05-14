/*
  The points covered by a (x,y,b) request are contained into the square
  [x-r,x+r]x[y-r,y+r] for r = b^(1/3) < 465 so that theoretically the problem
  could be brute-forced by enumerating covered points and using a set, a bloom
  filter, or an array + sort to eliminate duplicates. However this is too slow
  to pass on Kattis.
  The expected solution was a quadtree.
  We use an offline coordinates compression based approach here.
*/
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

#define CUBE(X) (abs((X)*(X)*(X)))
#define DIST3(X1,Y1,X2,Y2) ((CUBE((X1)-(X2)))+(CUBE((Y1)-(Y2))))
#define _x_ first
#define _y_ second

typedef vector< pair<int,int> > points;

void sort_uniq(vector<int> &T) {
  sort(T.begin(), T.end()); 
  auto last = unique(T.begin(), T.end());
  T.resize(distance(T.begin(), last));
}

int find_idx(vector<int> &T, int x) {
  return distance(T.begin(), find(T.begin(), T.end(), x));
}

int main() {
  int N,K;
  cin >> N >> K;
  vector<int> X(K),Y(K),B(K),R(K),AX,AY;
  for (int k=0; k<K; ++k) {
    cin >> X[k] >> Y[k] >> B[k];
    R[k] = pow(B[k]+1, 1./3.);
    AX.push_back(X[k]-R[k]);
    AX.push_back(X[k]+R[k]+1);
    AY.push_back(Y[k]-R[k]);
    AY.push_back(Y[k]+R[k]+1);
  }
  sort_uniq(AX);
  sort_uniq(AY);
  vector< vector<points> > Box(AX.size(), vector<points>(AY.size()));
  vector< vector<bool> > Used(AX.size(), vector<bool>(AY.size(), false));
  int s = 0;
  for (int k=0; k<K; ++k) {
    int i1 = find_idx(AX, X[k]-R[k]), i2 = find_idx(AX, X[k]+R[k]+1);
    int j1 = find_idx(AY, Y[k]-R[k]), j2 = find_idx(AY, Y[k]+R[k]+1);
    for (int i=i1; i<i2; ++i) {
      for (int j=j1; j<j2; ++j) {
	if (Used[i][j]) {
	  points NewBox;
	  for (const auto &p : Box[i][j]) {
	    if (DIST3(p._x_,p._y_,X[k],Y[k])>B[k])
	      NewBox.push_back(p);
	    else ++s;
	  }
	  Box[i][j] = NewBox;
	}
	else {
	  if (DIST3(AX[i],AY[j],X[k],Y[k])<=B[k] &&
	      DIST3(AX[i],AY[j+1]-1,X[k],Y[k])<=B[k] &&
	      DIST3(AX[i+1]-1,AY[j],X[k],Y[k])<=B[k] &&
	      DIST3(AX[i+1]-1,AY[j+1]-1,X[k],Y[k])<=B[k])
	    s += (AX[i+1]-AX[i])*(AY[j+1]-AY[j]);
	  else
	    for (int x=AX[i]; x<AX[i+1]; ++x)
	      for (int y=AY[j]; y<AY[j+1]; ++y) {
		if (CUBE(x-X[k])+CUBE(y-Y[k])>B[k])
		  Box[i][j].push_back(make_pair(x,y));
		else ++s;
	      }
	  Used[i][j] = true;
	}
      }
    }
  }
  cout << (N+1LL)*(N+1LL) - s << endl;
  return 0;
}
