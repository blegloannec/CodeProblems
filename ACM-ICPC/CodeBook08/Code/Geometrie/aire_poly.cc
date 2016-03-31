#include <vector>
using namespace std;
// retourne le DOUBLE de l'aire du polygone quelconque (non croise) poly
// donne dans le sens direct (dans l'autre sens, on renvoie l'oppose)
int aire_poly(const vector<point> &poly) {
  int aire = 0;
  for (int i = 2; i < (int)poly.size(); ++i)
    aire += det(poly[0], poly[i-1], poly[i]);
  return aire;
}
