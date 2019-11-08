/*
  Union of rectangles in O(n log n) using a segment tree to stock intervals for the sweepline.
  https://en.wikipedia.org/wiki/Segment_tree
*/
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;


/* ===== BEGIN IntervalSegmentTree ===== */
struct IntervalSegmentTree {
  unsigned int N = 0;
  vector<int> IntervalCount;
  vector<double> FullLength, CoveredLength;

  IntervalSegmentTree(const vector<double> &Length);

  double get_covered_length() const { return CoveredLength[1]; }

  void _interval_update(int p, int start, int span, int i, int j, int x);  // [i,j[
  void interval_insert(int l, int r) { _interval_update(1,0,N,l,r, 1); }   // [l,r[
  void interval_remove(int l, int r) { _interval_update(1,0,N,l,r,-1); }
};

IntervalSegmentTree::IntervalSegmentTree(const vector<double> &Length) {
  N = 1;
  while (N<Length.size()) N <<= 1;
  IntervalCount.resize(2*N,0);
  FullLength.resize(2*N,0.);
  for (unsigned int p=0; p<Length.size(); ++p) FullLength[N+p] = Length[p];
  for (int p=N-1; p>0; --p) FullLength[p] = FullLength[2*p]+FullLength[2*p+1];
  CoveredLength.resize(2*N,0.);
}

void IntervalSegmentTree::_interval_update(int p, int start, int span, int i, int j, int x) {
  if (start+span<=i || j<=start) return;
  if (i<=start && start+span<=j) IntervalCount[p] += x;
  else {
    _interval_update(2*p,start,span/2,i,j,x);
    _interval_update(2*p+1,start+span/2,span/2,i,j,x);
  }
  if (IntervalCount[p]>0) CoveredLength[p] = FullLength[p];
  else if (p<(int)N) CoveredLength[p] = CoveredLength[2*p]+CoveredLength[2*p+1];
  else CoveredLength[p] = 0.;
}
/* ===== END SegmentTree ===== */


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
  
  for (int i=0; i<(int)Y.size()-1; ++i) Y[i] = Y[i+1]-Y[i];
  Y.pop_back();
  IntervalSegmentTree Line(Y);
  double A = 0., x0;
  int e = 0;
  while (e<(int)Event.size()) {
    // current line x-coord
    double x = Event[e]._x_;
    // updating area from x0 to x
    if (e>0) A += Line.get_covered_length()*(x-x0);
    // updating sweepline
    while (e==0 || (e<(int)Event.size() && Event[e]._x_==x)) {
      int i = Event[e]._i_;
      if (X1[i]==x) Line.interval_insert(Y1idx[i], Y2idx[i]);
      else Line.interval_remove(Y1idx[i], Y2idx[i]);
      ++e;
    }
    // updating previous line x-coord
    x0 = x;
  }
  A = round(100.*A)/100.;
  printf("%.2lf\n", A);
  return 0;
}
