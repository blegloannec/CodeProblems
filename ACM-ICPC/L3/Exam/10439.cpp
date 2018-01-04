#include <iostream>
#include <cmath>
using namespace std;

const double Pi2 = 2*M_PI;
const double Err = 1e-4;

bool is_int(double x) {
  int i = round(x);
  return abs(((double)i)-x) < Err;
}

// PGCD flottant
double fpgcd(double a, double b) {
  return abs(b)<Err ? a : fpgcd(b,a-floor(a/b)*b);
}

int main() {
  int nb;
  cin >> nb;

  while (nb-->0) {
    double xa,xb,xc,ya,yb,yc;
    cin >> xa >> ya >> xb >> yb >> xc >> yc;
    
    double x1 = (xa+xb)/2, y1 = (ya+yb)/2;
    double x2 = (xb+xc)/2, y2 = (yb+yc)/2;
    double nx1 = ya-yb, ny1 = xb-xa;           // vecteurs normaux
    double nx2 = yb-yc, ny2 = xc-xb;
    double d = -nx1*ny2 + ny1*nx2;
    double t = (-ny2*(x2-x1) + nx2*(y2-y1))/d;
    double x0 = x1+t*nx1, y0 = y1+t*ny1;       // centre

    // angles
    double ta = atan2(ya-y0,xa-x0), tb = atan2(yb-y0,xb-x0), tc = atan2(yc-y0,xc-x0);
    double a1 = abs(tb-ta);
    double a2 = abs(tc-ta);

    // methode efficace par PGCD flottant
    // attention : pgcd(a1,a2) n'est pas necessairement un diviseur de 2pi
    // (par exemple a1 = a2 = 3pi/7 < pi)
    // c'est pourquoi on prend pgcd(2pi,a1,a2)
    cout << round(Pi2/fpgcd(Pi2,fpgcd(a1,a2))) << endl;

    /* 
    // methode bourrine (acceptable car n <= 200)
    int n = 3;
    while (!(is_int(n*a1/Pi2) && is_int(n*a2/Pi2))) ++n;
    cout << n << endl;
    */
  }

  return 0;
}
