/*
  "No three points lie on a line."
  the solution is then an infinitesimal rotation or translation
  of a line going through two stars 
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ent;

struct Vec {
  ent x,y;
  Vec(ent x, ent y) : x(x), y(y) {}
  // integer angle comparison
  ent comp(const Vec &V) const;
  Vec operator-(const Vec &V) const {return Vec(x-V.x,y-V.y);}
  bool operator<(const Vec &V) const {return comp(V)<0;}
};

ent Vec::comp(const Vec &V) const {
  if (V.y>=0 && 0>y) return 1;
  if (y>=0 && 0>V.y) return -1;
  if (y==0 && V.y==0) {
    if ((x>=0 && V.x>=0)||(x<=0 && V.x<=0)) return 0;
    return x>0 ? -1 : 1;
  }
  return -(x*V.y-y*V.x);  // det
}

ent det(const Vec &A, const Vec &B) {
  return A.x*B.y-A.y*B.x;
}

int N;
vector<int> V;
vector<Vec> P;

// O(N^2 log N) approach turning around each point
int solve_n2logn() {
  if (N==0) return 0;
  int W = 0;
  for (int i=0; i<N; ++i) W += V[i];
  int dmin = 1<<25, wmax = 0;
  for (int c=0; c<N; ++c) {
    vector< pair<Vec,int> > Pc;
    for (int k=0; k<N; ++k)     // center  c
      if (k!=c) Pc.push_back(make_pair(P[k]-P[c],k));
    sort(Pc.begin(),Pc.end());  // points around c
    int i = 0, j = 1;
    int w0 = V[Pc[i].second];
    while (i<N-1) {
      while (j!=i && det(Pc[i].first,Pc[j].first)>0) {
	w0 += V[Pc[j].second];
	++j;
	if (j==N-1) j = 0;
      }
      
      vector< pair<int,int> > parts {make_pair(w0,W-w0),make_pair(w0+V[c],W-w0-V[c]),make_pair(w0-V[Pc[i].second],W-w0+V[Pc[i].second]),make_pair(w0+V[c]-V[Pc[i].second],W-w0-V[c]+V[Pc[i].second])};
      for (auto it=parts.begin(); it!=parts.end(); ++it) {
	int w1 = it->first, w2 = it->second;
	int w = min(w1,w2), d = abs(w1-w2);
	if (d<dmin) {dmin = d; wmax = w;}
	else if (d==dmin && w>wmax) wmax = w;
      }
      
      w0 -= V[Pc[i].second];
      ++i;
    }
  }
  return wmax;
}

int main() {
  cin >> N;
  V.resize(N);
  for (int i=0; i<N; ++i) {
    ent x,y;
    cin >> x >> y >> V[i];
    P.push_back(Vec(x,y));
  }
  cout << solve_n2logn() << endl;
  return 0;
}
