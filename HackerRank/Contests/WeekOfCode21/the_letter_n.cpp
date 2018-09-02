#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Vec {
  int x,y;
  
  Vec(int x, int y) : x(x), y(y) {}
  
  // integer angle comparison
  // (as computing atan2 is too slow...)
  int comp(const Vec &V) const {
    if (V.y>=0 && 0>y) return -1;
    if (y>=0 && 0>V.y) return 1;
    if (y==0 && V.y==0) {
      if (x*V.x>=0) return 0;
      if (x>V.x) return -1;
      return 1;
    }
    return -(x*V.y-y*V.x);  // det
  }
  
  bool operator<(const Vec &V) const {
    return comp(V)<0;
  }
};

int main() {
  int N;
  cin >> N;
  vector<Vec> P;
  for (int i=0; i<N; ++i) {
    int x,y;
    cin >> x >> y;
    P.push_back(Vec(x,y));
  }
  vector< vector<Vec> > Q(N);
  // O(N^2 log N) precomp
  for (int a=0; a<N; ++a) {
    // Q[a] = angle-sorted points around P[a]
    for (int b=0; b<N; ++b)
      if (b!=a) Q[a].push_back(Vec(P[b].x-P[a].x,P[b].y-P[a].y));
    sort(Q[a].begin(),Q[a].end());
  }
  // O(N^2 log N) comp
  long long res = 0;
  for (int b=0; b<N; ++b) {      // point B of the N
    for (int c=b+1; c<N; ++c) {  // point C
      // counting possible points A by dicho search in Q[b]
      Vec BC(P[c].x-P[b].x,P[c].y-P[b].y);
      Vec lBC(BC.y,-BC.x);
      int i = distance(Q[b].begin(),lower_bound(Q[b].begin(),Q[b].end(),lBC));
      int j = distance(Q[b].begin(),lower_bound(Q[b].begin(),Q[b].end(),BC));
      long long nbA = j>=i ? j-i : N-1-(i-j);
      if (nbA==0) continue;
      // counting possible points D by dicho search in Q[c]
      Vec CB(-BC.x,-BC.y);
      Vec lCB(CB.y,-CB.x);
      i = distance(Q[c].begin(),lower_bound(Q[c].begin(),Q[c].end(),lCB));
      j = distance(Q[c].begin(),lower_bound(Q[c].begin(),Q[c].end(),CB));
      long long nbD = j>=i ? j-i : N-1-(i-j);
      res += nbA*nbD;
    }
  }
  cout << res << endl;
  return 0;
}
