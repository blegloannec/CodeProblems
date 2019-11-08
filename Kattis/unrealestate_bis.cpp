/*
  Union of rectangles in O(n^2) using a vector for the sweepline.
  This approach could be optimized in O(n log n) replacing the
  vector by a segment tree (see unrealestate_ter.cpp).
*/
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

#define _x_ first
#define _y_ first
#define _i_ second

int main() {
  int N;
  scanf("%d", &N);
  vector<double> X1(N),Y1(N),X2(N),Y2(N),Y;
  vector< pair<double,int> > Event,Ydup;
  vector<int> Y1idx(N),Y2idx(N);
  for (int i=0; i<N; ++i) {
    scanf("%lf %lf %lf %lf", &X1[i], &Y1[i], &X2[i], &Y2[i]);
    Event.push_back(make_pair(X1[i],i));
    Event.push_back(make_pair(X2[i],i));
    Ydup.push_back(make_pair(Y1[i],i));
    Ydup.push_back(make_pair(Y2[i],i));
  }  
  sort(Event.begin(), Event.end());
  sort(Ydup.begin(), Ydup.end());
  for (int i=0; i<(int)Ydup.size(); ++i) {
    double y = Ydup[i]._y_;
    int idx = Ydup[i]._i_;
    if (i==0 || y!=Ydup[i-1]._y_) Y.push_back(y);
    if (y==Y1[idx]) Y1idx[idx] = (int)Y.size()-1;
    else Y2idx[idx] = (int)Y.size()-1;
  }
  
  vector<int> Line(Y.size(),0);
  double A = 0., x0;
  int e = 0;
  while (e<(int)Event.size()) {
    // current line x-coord
    double x = Event[e]._x_;
    // updating area from x0 to x
    if (e>0)
      for (int i=0; i<(int)Line.size(); ++i)
	if (Line[i]>0)
	  A += (Y[i+1]-Y[i])*(x-x0);
    // updating sweepline
    while (e==0 || (e<(int)Event.size() && Event[e]._x_==x)) {
      int i = Event[e]._i_;
      if (X1[i]==x)
	for (int j=Y1idx[i]; j<Y2idx[i]; ++j)
	  ++Line[j];
      else
	for (int j=Y1idx[i]; j<Y2idx[i]; ++j)
	  --Line[j];
      ++e;
    }
    // updating previous line x-coord
    x0 = x;
  }
  A = round(100.*A)/100.;
  printf("%.2lf\n", A);
  return 0;
}
