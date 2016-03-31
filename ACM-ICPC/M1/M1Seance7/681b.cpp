#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

struct point {
  int x, y;
  point(int a_x, int a_y): x(a_x), y(a_y) {}
};

point *pivot_enveloppe_convexe;
vector<point> src;
stack<point*> dst;
vector<point*> dst2;

// calcule det(p2-p1, p3-p1), positif si p1, p2, p3 dans le sens direct
int det(const point &p1, const point &p2, const point &p3) {
  return (p2.x-p1.x)*(p3.y-p1.y)-(p2.y-p1.y)*(p3.x-p1.x);
}

void enveloppe_convexe(vector<point> &src, stack<point*> &dst) {
  int sz = src.size();
  int min = 0;
  point *p1, *p2, *p3;
  
}

int miroir() {
  dst2.clear();
  int res = 0;
  while (!dst.empty()) {
    dst2.push_back(dst.top());
    dst.pop();
    ++res;
  }
  return res;
}

int main() {
  int cas,n,x,y;
  cin >> cas;
  cout << cas << '\n';
  for (int j=0; j<cas; ++j) {
    cin >> n;
    for (int i=0; i<n; ++i) {
      cin >> x >> y;
      if (i<n-1) src.push_back(point(x,y));
    }
    enveloppe_convexe(src,dst);
    dst.pop();
    int res = miroir();
    //if (res<2) cout << "0\n";
    //else {
      cout <<  res+1 << '\n';
      int start = 0;
      for (int i=1; i<res; ++i) {
	if (dst2[i]->y < dst2[start]->y) start = i;
	else if (dst2[i]->y == dst2[start]->y && dst2[i]->x < dst2[start]->x) start = i;
      }
      for (int i=0; i<=res; ++i) {
	cout << dst2[(start-i+res)%res]->x << ' ' << dst2[(start-i+res)%res]->y << '\n';
      }
      //}
    src.clear();
    cin >> x;
    if (j < cas-1) cout << "-1\n";
  }
  return 0;
}
