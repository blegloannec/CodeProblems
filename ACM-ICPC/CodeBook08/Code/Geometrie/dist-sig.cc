#include <cmath>
// retourne la "distance signee" entre le point p et la droite (a, b)
// le signe indique dans quel demi plan defini par la droite se trouve le point
// requires a != b;
double distance_sig(point &p, point &a, point &b) {
  int x, y, c;
  x = a.y-b.y;
  y = b.x-a.x;
  c = -x*a.x-y*a.y;
  return (p.x*x + p.y*y + c)/sqrt(x*x + y*y);
}
