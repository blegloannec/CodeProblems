#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

typedef long double flott;

#define RANGE 1e-9

int main() {
  flott m,M,x,y,z,s,s2,xmax,delta,f,y2;
  cin >> m >> M;

  for (s=m; s<=M; s+=0.01) {
    xmax = min(s/3,pow(s,(flott)1./3.))+0.01;
    for (x=0.01; x<=xmax; x+=0.01) {
      s2 = s-x;
      delta = s2*s2 - 4*s/x;
      if (delta >= -RANGE) {
	if (delta <= RANGE) delta = 0;
	y = (s2-sqrt(delta))/2;
	if (x>y+RANGE) continue;
	y2 = 100*y;
	f = fabs(y2-round(y2));
	if (f <= 100*RANGE) {
	  z = s2-y;
	  printf("%.2Lf = %.2Lf + %.2Lf + %.2Lf = %.2Lf * %.2Lf * %.2Lf\n",s,x,y,z,x,y,z);
	}
      }
    }
  }
 
  return 0;
}
