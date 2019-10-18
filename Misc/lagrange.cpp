#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

typedef long long ent;
typedef pair<ent,ent> point;

ent gcd(ent a, ent b) {
  return b==0 ? a : gcd(b,a%b);
}

struct Fraction {
  ent p,q;
  
  Fraction(ent p0=0) {
    p = p0;
    q = 1;
  }
  
  Fraction(ent p0, ent q0) {
    assert(q0!=0);
    ent g = gcd(p0,q0);
    p = p0/g;
    q = q0/g;
    if (q<0) {
      p = -p;
      q = -q;
    }
  }
  
  Fraction operator+(const Fraction &B) const {
    return Fraction(p*B.q+B.p*q, q*B.q);
  }
  
  Fraction operator-(const Fraction &B) const {
    return Fraction(p*B.q-B.p*q, q*B.q);
  }
  
  Fraction operator-() const {
    return Fraction(-p, q);
  }
  
  Fraction operator*(const Fraction &B) const {
    return Fraction(p*B.p, q*B.q);
  }
  
  Fraction operator/(const Fraction &B) const {
    return Fraction(p*B.q, q*B.p);
  }
  
  bool operator<(const Fraction &B) const {
    return p*B.q < q*B.p;
  }
  
  bool operator==(const Fraction &B) const {
    return p==B.p && q==B.q;
  }
  
  void print() const {
    cout << p << '/' << q << endl;
  }
};

/*
  Calcul des coefficients du polynome de Lagrange en O(n^2)

  Soit P = {(xi,yi)}_i un ensemble de n points verifiant
  xi =/= xj pour tous i =/= j.
  L = Sum_i( yi * Prod_{j=/=i} (X-xj) / (xi-xj) )
  Cette representation permet d'evaluer L en un point en O(n^2).

  On pose Q = Prod_{i} (X-xi), que l'on peut evaluer en un point en O(n),
  et ci = yi * Prod_{j=/=i} 1/(xi-xj), chaque ci se pre-calcule en O(n)
  et donc l'ensemble des ci en O(n^2).
  Alors L = Sum_i( ci * Q / (X-xi) )
  Avec les pre-calculs en O(n^2), cette representation permet d'evaluer
  L en O(n) par valeur (evaluation de Q(x) en O(n) puis evaluation de L(x)
  en O(n) grace aux ci pre-calcules).

  Si l'on veut explicitement les coefficients de L, on peut
  calculer explicitement les coefficients de Q en O(n^2), chaque
  terme de L se calcule alors en O(n) par division euclidienne de Q
  par X-xi. Calculer ces n termes de degre n et les sommer coute O(n^2).
  On a ainsi calcule L explicitement en O(n^2) (contre O(n^3) avec la
  formule initiale).
*/

vector<Fraction> lagrange(vector<point> &P) {
  int n = P.size();
  // calcul explicite de Q en O(n^2)
  vector<Fraction> Q(n+1);
  Q[0] = Fraction(1);
  for (int i=0; i<n; ++i) {
    // Q *= X-xi
    Fraction xi(P[i].first);
    for (int j=i+1; j>=0; --j)
      Q[j] = (j>0 ? Q[j-1] : 0) - xi*Q[j];
  }
  // calcul explicite de L en O(n^2)
  vector<Fraction> L(n);
  for (int i=0; i<n; ++i) {
    ent xi = P[i].first, yi = P[i].second;
    Fraction pi(yi);
    for (int j=0; j<n; ++j) {
      if (i==j) continue;
      ent xj = P[j].first;
      pi = pi*Fraction(1,xi-xj);
    }
    // DE Q/(X-xi) et ajout direct a L
    vector<Fraction> R = Q;
    for (int j=n; j>0; --j) {
      R[j-1] = R[j-1] + R[j]*xi;
      L[j-1] = L[j-1] + pi*R[j];
    }
  }
  return L;
}

int main() {
  vector<point> P = {make_pair(1,1), make_pair(2,3), make_pair(5,2), make_pair(8,7), make_pair(13,43), make_pair(15,187), make_pair(25,800)};
  vector<Fraction> L = lagrange(P);
  for (unsigned int i=0; i<L.size(); ++i)
    L[i].print();
  return 0;
}
