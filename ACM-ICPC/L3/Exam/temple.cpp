#include <iostream>
#include <cmath>
using namespace std;

typedef double flott; 

flott pgcd(flott a, flott b) {
  if (fabs(b)<=0.00001) return a;
  return pgcd(b, fabs(fabs(a)-fabs(b)));
}

int main() {
  int nb,v1,v2;
  flott xa,xb,xc,ya,yb,yc,xab,yab,xbc,ybc,xn,xm,yn,ym,t,x0,y0,r2,nab,nbc;
  flott alpha1,alpha2,sin1,cos1,sin2,cos2;
  flott pi = 3.141592654;
  cin >> nb;

  while (nb-->0) {
    cin >> xa >> ya >> xb >> yb >> xc >> yc;
    xab = xb-xa;
    yab = yb-ya;
    nab = sqrt(xab*xab+yab*yab);
    xab = xab/nab;
    yab = yab/nab;
    xbc = xc-xb;
    ybc = yc-yb;
    nbc = sqrt(xbc*xbc+ybc*ybc);
    xbc = xbc/nbc;
    ybc = ybc/nbc;
    xm = (xa+xb)/2;
    ym = (ya+yb)/2;
    xn = (xc+xb)/2;
    yn = (yc+yb)/2;
    t = (xm-xn+(ym-yn)*ybc/xab)/(yab-xab*ybc/xbc);
    x0 = xm - t*yab;
    y0 = ym + t*xab;

    cout << "x0, y0 " << x0 << " " << y0 << "\n";
    
    r2 = (xa-x0)*(xa-x0)+(ya-y0)*(ya-y0);
    sin1 = -((xa-x0)*(yb-y0)-(xb-x0)*(ya-y0))/r2;
    cos1 = ((xa-x0)*(xb-x0)+(ya-y0)*(yb-y0))/r2;
    alpha1 = acos(cos1);
    if (sin1<0) alpha1 = 2*pi - alpha1;
    sin2 = ((xc-x0)*(yb-y0)-(xb-x0)*(yc-y0))/r2;
    cos2 = ((xc-x0)*(xb-x0)+(yc-y0)*(yb-y0))/r2;
    alpha2 = acos(cos2);   
    if (sin2<0) alpha2 = 2*pi - alpha2;

   cout << "alpha1, alpha2, " << alpha1 << " " << alpha2 << "\n";

    
    cout << (int) 2*pi/(pgcd(alpha1,alpha2)) << '\n';
  }

  return 0;
}
