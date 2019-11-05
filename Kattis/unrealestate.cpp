/*
  Union of rectangles in O(n^2) using a multiset for the sweepline.
  (slower than the vector variant unrealestate_bis.cpp)
*/
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

#define _x_ first
#define _y_ first
#define _i_ second

int main() {
  int N;
  scanf("%d", &N);
  vector<double> X1(N),Y1(N),X2(N),Y2(N);
  vector< pair<double,int> > Event;
  for (int i=0; i<N; ++i) {
    scanf("%lf %lf %lf %lf", &X1[i], &Y1[i], &X2[i], &Y2[i]);
    Event.push_back(make_pair(X1[i],i));
    Event.push_back(make_pair(X2[i],i));
  }
  sort(Event.begin(), Event.end());
  
  multiset< pair<double,int> > Line;
  double A=0., x0;
  int e = 0;
  while (e<(int)Event.size()) {
    double x = Event[e]._x_;
    if (e==0) x0 = x;
    
    int cnt = 0;
    double y0;
    for (const auto &I : Line) {
      if (cnt==0) y0 = I.first;
      else if (cnt==1 && I.second==-1) A += (I._y_-y0)*(x-x0);
      cnt += I.second;
    }
    
    while (e==0 || (e<(int)Event.size() && Event[e]._x_==x)) {
      int i = Event[e]._i_;
      if (X1[i]==x) {
	Line.insert(make_pair(Y1[i],1));
	Line.insert(make_pair(Y2[i],-1));
      }
      else {
	Line.erase(Line.find(make_pair(Y1[i],1)));
	Line.erase(Line.find(make_pair(Y2[i],-1)));
      }
      ++e;
    }
    
    x0 = x;
  }
  A = round(100.*A)/100.;
  printf("%.2lf\n", A);
  return 0;
}
