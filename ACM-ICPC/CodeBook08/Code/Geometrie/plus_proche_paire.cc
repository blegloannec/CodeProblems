#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
#define MAX 100000000
struct point {
  double x, y;
};
bool cmpx(const point &a, const point &b) {
  return a.x < b.x;
}
bool cmpy(const point *a, const point *b) {
  return a->y < b->y;
}
inline double dist2(const point &a, const point &b) {
  return (b.x-a.x)*(b.x-a.x)+(b.y-a.y)*(b.y-a.y);
}
double aux(const vector<point> &v, int deb, int fin) {
  int milieu;
  double l, mini = MAX+1;
  vector <const point*> vy;
  if ((fin-deb) < 4) {
    for (int i = deb; i < fin; ++i)
      for (int j = i+1; j < fin; ++j)
        mini = min(mini, dist2(v[i], v[j]));
    return mini;
  }
  milieu = deb+(fin-deb)/2;
  mini = min(aux(v, deb, milieu), aux(v, milieu, fin));
  l = v[milieu].x;
  for (int i = deb; i < fin; ++i)
    if ((v[i].x-l)*(v[i].x-l) <= mini)
      vy.push_back(&(v[i]));
  sort(vy.begin(), vy.end(), cmpy);
  for (int i = 0; i < (int)vy.size(); ++i)
    for (int j = i+1; j < i+7 && j < (int)vy.size(); ++j)
      mini = min(mini, dist2(*(vy[i]), *(vy[j])));
  vy.clear();
  return mini;
}
// requires v.size() >= 2;
// ensures permut(v, \old(v));
double plus_proche_paire(vector<point> &v) {
  sort(v.begin(), v.end(), cmpx);
  return sqrt(aux(v, 0, (int)v.size()));
}
