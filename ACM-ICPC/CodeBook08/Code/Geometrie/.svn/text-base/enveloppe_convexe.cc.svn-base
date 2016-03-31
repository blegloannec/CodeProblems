#include <algorithm>
#include <vector>
#include <stack>
using namespace std;
point *pivot_enveloppe_convexe;
bool comp(const point &p1, const point &p2) {
  return det(*pivot_enveloppe_convexe, p1, p2) > 0;
}
// calcul de l'enveloppe convexe du polygone quelconque (non croise) src
// requires src.size() >= 1;
// ensures permut(\old(src), src)
//   && dst dans l'ordre direct du fond vers le sommet de la pile;
// ATTENTION : le premier point est repete a la fin dans dst
void enveloppe_convexe(vector<point> &src, stack<point*> &dst) {
  int sz = src.size();
  int min = 0;
  point *p1, *p2, *p3;
  // on prend le point le plus a gauche comme point de depart
  for (int i = 1; i < (int)src.size(); ++i)
    if (src[i].x < src[min].x) min = i;
  swap(src[0], src[min]);
  pivot_enveloppe_convexe = &(src[0]);
  sort(src.begin()+1, src.end(), comp);
  src.push_back(src[0]);
  p2 = &(src[0]); p3 = &(src[1]);
  dst.push(p2); dst.push(p3);
  for (int i = 2; i <= sz; ++i) {
    p1 = p2; p2 = p3; p3 = &(src[i]);
    while (det(*p1, *p2, *p3) < 0) {
      dst.pop();
      p2 = dst.top();
      if (dst.size() == 1) break;
      dst.pop();
      p1 = dst.top();
      dst.push(p2);
    }
    dst.push(p3);
  }
  src.pop_back();
}
