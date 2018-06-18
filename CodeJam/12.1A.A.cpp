#include <iostream>
using namespace std;

#define AMAX 100000 

int T,A,B;
double p[AMAX];
// Produits des p_i :
double prodp[AMAX];

double E1() {
  double Pgood = prodp[A-1];
  return Pgood*(B-A+1)+(1-Pgood)*(2*B-A+2);
}

double E2(int nbback) {
  double Pgood = prodp[A-nbback-1];
  return Pgood*(2*nbback+B-A+1)+(1-Pgood)*(2*nbback+2*B-A+2);
}

double E3() {
  return B+2.0;
}

int main() {
  cout.precision(6);
  cout << fixed;
  double E;
  cin >> T;
  for (int c=1; c<=T; ++c) {
    cin >> A >> B;
    for (int i=0; i<A; ++i)
      cin >> p[i];
    prodp[0] = p[0];
    for (int i=1; i<A; ++i)
      prodp[i] = prodp[i-1]*p[i];
    E = E1();
    for (int i=1; i<=A; ++i) 
      E = min(E,E2(i));
    E = min(E,E3());
    cout << "Case #" << c << ": " << E << endl;
  }
}
