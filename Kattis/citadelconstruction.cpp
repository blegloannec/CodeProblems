/*
  O(n^2 log n) approach
  The max area quadrilateral vertices lie on the convex hull.
  For each diagonal of the convex hull, ternary search for the
  max triangle on both sides.
  NB: http://commissies.ch.tudelft.nl/chipcie/archief/2014/bapc/solutions.pdf
      This was the expected approach, O(n^2) and O(n log n) approaches exist
      but I don't know them...
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct point {
  int x,y;
  point(int x, int y) : x(x), y(y) {}
  point operator-(const point &A) const {
    return point(x-A.x, y-A.y);
  }
  int operator*(const point &A) const {
    return x*A.y - y*A.x;
  }
  bool operator<(const point &A) const {
    return x<A.x || (x==A.x && y<A.y);
  }
};

typedef vector<point> points;

bool left_turn(const point &A, const point &B, const point &C) {
  return (A-C)*(B-C)>0;
}

points andrew(points &S) {  // convex hull
  points top, bot;
  sort(S.begin(), S.end());
  for (const point &p : S) {
    while (top.size()>=2 && !left_turn(p,top[top.size()-1],top[top.size()-2]))
      top.pop_back();
    top.push_back(p);
    while (bot.size()>=2 && !left_turn(bot[bot.size()-2],bot[bot.size()-1],p))
      bot.pop_back();
    bot.push_back(p);
  }
  bot.pop_back();
  bot.insert(bot.end(), top.rbegin(), top.rend()-1);
  return bot;
}

int ternary_search(const points &P, const int a, int b) {
  int N = P.size();
  point AB = P[b]-P[a];
  if (b<a) b += N;
  int l = a+1, r = b-1;
  while (l<r) {
    int m1 = (l+r)/2;
    int m2 = m1+1;
    int t1 = (P[m1%N]-P[a])*AB, t2 = (P[m2%N]-P[a])*AB;
    if (t1>t2) r = m1;
    else l = m2;
  }
  return (P[l%N]-P[a])*AB;
}

int max_quad(points &P) {
  points H = andrew(P);
  int N = H.size(), res = 0;
  for (int i=0; i<N; ++i)
    for (int j=i+2; j<N; ++j)
      res = max(res, ternary_search(H,i,j)+ternary_search(H,j,i));
  return res;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int N;
    cin >> N;
    points P;
    P.reserve(N);
    for (int i=0; i<N; ++i) {
      int x,y;
      cin >> x >> y;
      P.push_back(point(x,y));
    }
    int res = max_quad(P);
    if (res%2==0) cout << res/2 << '\n';
    else cout << res/2 << ".5\n";
  }
  return 0;
}
