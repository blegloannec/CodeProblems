#include <limits.h>
#include <algorithm>
#include <vector>
using namespace std;
// retourne vrai ssi l'intersection des interieurs
// des polygones convexes p1 et p2 est non vide
bool inter_poly_convexe(const vector<point> &p1, const vector<point> &p2) {
  const vector<point> *p[2] = {&p1, &p2};
  int sz[2] = {p1.size(), p2.size()};
  double dist, left[2], right[2];
  for (int i = 0; i < 2; ++i) {  // pour les deux polygones
    for (int j = 0; j < sz[i]; ++j) {  // pour chaque cote, projection
      left[0] = left[1] = INT_MAX;
      right[0] = right[1] = INT_MIN;
      for (int k = 0; k < 2; ++k)
        for (int l = 0; l < sz[k]; ++l) {
          dist = distance_sig((*p[k])[l], (*p[i])[j], (*p[i])[(j+1)%sz[i]]);
          left[k] = min(left[k], dist);
          right[k] = max(right[k], dist);
        }
      // si les deux ouverts ne se recouvrent pas
      if (!(left[0] < left[1] && right[0] > left[1]
            || left[0] == left[1]
            || left[0] > left[1] && right[1] > left[0]))
        return false;
  } }
  return true;
}
