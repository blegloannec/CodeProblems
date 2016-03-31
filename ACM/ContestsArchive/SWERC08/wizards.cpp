// 2h

#include <iostream>
#include <algorithm>
using namespace std;

typedef double flott;

typedef flott *poly;

#define MAX 12

flott P[MAX];
flott PP[MAX];
int d_P, d_PP;

#define RANGE (1e-6)


flott abs(flott f) {
  return (f<0) ? -f : f;
}

void MOD_poly(poly P, int &d_P, poly Q, int &d_Q) {
  while (d_P>=d_Q) {
    int d = d_P - d_Q;
    flott c = P[d_P]/Q[d_Q];
    --d_P;
    for (int i=d_Q-1; i>=0; --i) {
      P[i+d] -= Q[i]*c;
    }
  }
}

void affich(poly P, int d_P) {
  for (int i=0; i<=d_P; ++i) 
    cout << P[i] << ' ';
  cout << endl;
}

int GCD_poly(poly P, int &d_P, poly Q, int &d_Q) {
  if (d_Q < 0) {
    //affich(P,d_P);
    return d_P;
  }
  else {
    MOD_poly(P,d_P,Q,d_Q);
    while ((d_P>=0)&&(abs(P[d_P])<RANGE)) --d_P;
    // on normalise :
    if (abs(P[d_P])<RANGE) P[d_P] = 0;
    else {
      flott c = 1/P[d_P];
      for (int i=0; i<=d_P; ++i) 
	P[i] *= c;
    }
    //affich(P,d_P);
    return GCD_poly(Q,d_Q,P,d_P);
  }
}


bool constante(poly P, int d_P) {
  flott tmp;
  for (int i=1; i<=d_P; ++i) {
    if (abs(tmp)>RANGE) return false;
  }
  return true;
}


int main() {
  int t,n,a;
  cin >> t;
  while (t-->0) {
    cin >> n;
    d_P = n;
    d_PP = n-1;
    for (int i=0; i<=n; ++i) {
      cin >> a;
      P[n-i] = (flott)a;
      if (i<n) PP[n-1-i] = (flott)((n-i)*a);
    }
    if (!(GCD_poly(P,d_P,PP,d_PP)==0)) cout << "No!\n";
    else cout << "Yes!\n";
  }
  return 0;
}
