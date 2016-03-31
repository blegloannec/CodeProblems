#include <cmath>
// retourne la "distance" entre le point p et la droite (a, b)
// requires a != b;
double distance(const point &p, const point &a, const point &b) {
  int x, y, c;
  x = a.y-b.y;
  y = b.x-a.x;
  c = -x*a.x-y*a.y;
  return abs(p.x*x + p.y*y + c)/sqrt(x*x + y*y);
}
