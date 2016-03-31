#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <cmath>
using namespace std;

struct point {
  int x, y;
  point(int a_x, int a_y): x(a_x), y(a_y) {}
};

point *pivot_enveloppe_convexe;
vector<point> src,src2;
stack<point*> dst;


// calcule det(p2-p1, p3-p1), positif si p1, p2, p3 dans le sens direct
int det(const point &p1, const point &p2, const point &p3) {
  return (p2.x-p1.x)*(p3.y-p1.y)-(p2.y-p1.y)*(p3.x-p1.x);
}

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

// retourne le DOUBLE de l'aire du polygone quelconque (non croise) poly
// donne dans le sens direct (dans l'autre sens, on renvoie l'oppose)
int aire_poly(const vector<point> &poly) {
  int d, aire = 0;
  for (int i = 2; i < (int)poly.size(); ++i) {
    d = det(poly[0], poly[i-1], poly[i]);
    //if (d > 0) 
      aire += d;
      // else aire -= d;
  }
  return aire;
}


int main() {
  int n,x,y,cas,a,b;
  double res;
  cas = 1;
  while(cin >> n){
    if(n == 0) return 0;
    for (int i=0; i<n; ++i) {
      cin >> x >> y;
      src.push_back(point(x,y));
    }
    a = aire_poly(src);
    if (a < 0) a = -a;
    enveloppe_convexe(src,dst);
    dst.pop();
    while (!dst.empty()) {
      src2.push_back(*(dst.top()));
      dst.pop();
    }
    b = aire_poly(src2);
    if (b < 0) b = -b;
    res = (double)round(((double)b-(double)a)*10000.0/(double)b)/100.0;
    cout << "Tile #" << cas << '\n';
    printf("Wasted Space = %.2f \%\n",res);
    ++cas;
    src.clear();
    src2.clear();
    cout << '\n';
  }
  return 0;
}
