#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;
using ent = int;

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

int N;
vector<ent> X,Y;

int max_colinear() {
  if (N<=2) return N;
  Fraction Inf(0); Inf.q = 0;
  int res = 1;
  for (int i=0; i<N; ++i) {
    vector<Fraction> Slopes;
    for (int j=i+1; j<N; ++j)
      if (X[i]==X[j]) Slopes.push_back(Inf);
      else Slopes.push_back(Fraction(Y[j]-Y[i], X[j]-X[i]));
    sort(Slopes.begin(), Slopes.end());
    int curr = 1;
    for (int k=1; k<(int)Slopes.size(); ++k)
      if (Slopes[k]==Slopes[k-1]) res = max(res, ++curr);
      else curr = 1;
  }
  return res+1;
}

int main() {
  while (true) {
    scanf("%d", &N);
    if (N<=0) break;
    X.resize(N); Y.resize(N);
    for (int i=0; i<N; ++i) scanf("%d %d", &X[i], &Y[i]);
    printf("%d\n", max_colinear());
  }
  return 0;
}
