#include <iostream>
using namespace std;

typedef double flot;

const flot eps = 0.01;

int main() {
  int T;
  flot A,B,C;
  flot x0,y0,x,y;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> A >> B >> C;
    cin >> x0 >> y0 >> x >> y;
    flot dx = x-x0;
    flot dy = y-y0;
    int cpt = 0;
    while (!(y>=0 && -eps<=x && x<=eps)) {
      flot ex = B*y;
      flot ey = -A*x;
      flot de = (dx*ex+dy*ey)/(ex*ex+ey*ey);
      dx -= 2.*de*ex;
      dy -= 2.*de*ey;
      flot a = A*dx*dx + B*dy*dy;
      flot b = 2.*(A*x*dx + B*y*dy);
      x -= b*dx/a;
      y -= b*dy/a;
      ++cpt;
    }
    cout << cpt << endl;
  }
}
