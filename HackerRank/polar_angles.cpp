#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


struct Vec {
  int x,y;
  
  Vec(int x, int y) : x(x), y(y) {}
  
  // integer angle comparison
  int comp(const Vec &V) const;
  int norm2() const {return x*x+y*y;}
  
  bool operator<(const Vec &V) const {
    int c = comp(V);
    return c==0 ? norm2()<V.norm2() : c<0;
  }
};

int Vec::comp(const Vec &V) const {
  if (V.y>=0 && 0>y) return 1;
  if (y>=0 && 0>V.y) return -1;
  if (y==0 && V.y==0) {
    if ((x>=0 && V.x>=0)||(x<=0 && V.x<=0)) return 0;
    return x>0 ? -1 : 1;
  }
  return -(x*V.y-y*V.x);  // det
}


int main() {
  int N;
  cin >> N;
  vector<Vec> P;
  for (int i=0; i<N; ++i) {
    int x,y;
    cin >> x >> y;
    P.push_back(Vec(x,y));
  }
  sort(P.begin(),P.end());
  for (int i=0; i<N; ++i)
    cout << P[i].x << ' ' << P[i].y << endl;
  return 0;
}
